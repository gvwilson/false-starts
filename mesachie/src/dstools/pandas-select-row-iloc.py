import pandas as pd

packages = pd.read_csv("python-local-package-size.csv")
print(packages.iloc[0])
print(packages.iloc[0:5])
print(packages["Characters"][0:3])
print(packages.iloc[0:3]["Characters"])
