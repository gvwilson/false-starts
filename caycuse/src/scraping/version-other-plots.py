import sys

import pandas as pd
import plotly.express as px

datafile = sys.argv[1]
packages = pd.read_csv(datafile)

slice = packages[packages["Releases"] < 100]
fig = px.violin(slice, y="Releases", width=600, height=400)
fig.show()
fig.write_image("release-count-violin.svg")

fig = px.box(slice, y="Releases", width=600, height=400)
fig.show()
fig.write_image("release-count-box.svg")
