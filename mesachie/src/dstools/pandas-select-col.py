import pandas as pd

packages = pd.read_csv("python-local-package-size.csv")
print(packages["Path"])

print(packages[["Lines", "Characters"]])

print(packages[0])
