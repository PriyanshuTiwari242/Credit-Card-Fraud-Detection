import pandas as pd

df = pd.read_csv("creditcard.csv")

normal = df[df["Class"] == 0]

print(normal.drop("Class", axis=1).iloc[0].tolist())