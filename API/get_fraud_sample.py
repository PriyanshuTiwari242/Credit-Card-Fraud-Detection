import pandas as pd

df = pd.read_csv("creditcard.csv")

fraud = df[df["Class"] == 1]

print(fraud.drop("Class", axis=1).iloc[0].tolist())