import sys

import numpy as np
import pandas as pd

datafile = sys.argv[1]
packages = pd.read_csv(datafile)
print(packages["Releases"].agg(["mean", "median", "var", "std", "min", "max"]))
