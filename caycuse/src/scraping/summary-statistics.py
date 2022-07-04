import sys

import pandas as pd

datafile = sys.argv[1]
packages = pd.read_csv(datafile)
print(packages["Releases"].agg(["mean", "median", "var", "std", "min", "max"]))
