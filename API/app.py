import sqlite3
from flask import redirect
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import Flask, request, jsonify, send_from_directory, render_template, session
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "my_super_secret_key"
bcrypt = Bcrypt(app)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")   # 👈 serves HTML

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]

        print("Received:", data)   # 👈 debug

        # ✅ check length
        if len(data) != 30:
            return jsonify({"error": f"Expected 30 values, got {len(data)}"})

        # ✅ check invalid values
        if any(v is None for v in data):
            return jsonify({"error": "Invalid input values"})

        data = np.array(data).reshape(1, -1)

        print("Before scaling:", data)   # 👈 debug

        data = scaler.transform(data)

        prediction = model.predict(data)
        # Convert prediction to readable text           
        result = "Fraud" if prediction[0] == 1 else "Safe"
        timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        # Save prediction history
        if "user" in session:

           conn = sqlite3.connect("users.db")
           cursor = conn.cursor()

           cursor.execute(
               """
               INSERT INTO predictions
               (username, result, timestamp)
               VALUES (?, ?, ?)
               """,
               (session["user"], result, timestamp)
                 )
           conn.commit()
           conn.close()

        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        print("ERROR:", e)   # 👈 THIS WILL SHOW REAL PROBLEM
        return jsonify({"error": str(e)})


@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]

        import pandas as pd
        df = pd.read_csv(file)

        # drop target column if present
        if "Class" in df.columns:
            df = df.drop("Class", axis=1)

        data = scaler.transform(df)
        predictions = model.predict(data)

        # count fraud vs non-fraud
        fraud = int(sum(predictions))
        normal = int(len(predictions) - fraud)

        return jsonify({
            "total": len(predictions),
            "fraud": fraud,
            "normal": normal
        })

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, hashed_password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            stored_password = user[3]

            if bcrypt.check_password_hash(
                stored_password,
                password
            ):
                session["user"] = user[1]
                return redirect("/dashboard")

            else:
                return "Wrong Password ❌"

        return "User Not Found ❌"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return "Please Login First"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT result FROM predictions WHERE username=?",
        (session["user"],)
    )

    rows = cursor.fetchall()

    conn.close()

    total = len(rows)

    fraud = sum(1 for row in rows if row[0] == "Fraud")

    safe = total - fraud

    return render_template(
        "dashboard.html",
        username=session["user"],
        total_predictions=total,
        fraud_count=fraud,
        safe_count=safe
    )

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")

@app.route("/history")
def history():

    if "user" not in session:
        return "Please Login First"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM predictions
        WHERE username = ?
        """,
        (session["user"],)
    )

    rows = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        rows=rows
    )

if __name__ == "__main__":
    app.run(debug=True)