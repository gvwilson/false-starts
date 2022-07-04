import pandas as pd

colors = pd.DataFrame(
    columns=["name", "red", "green", "blue"],
    data=[
        ["yellow", 1.0, 1.0, 0.0],
        ["aqua", 0.0, 1.0, 1.0],
        ["fuchsia", 1.0, 0.0, 1.0],
    ],
)
print(colors)

red = colors["red"]
print(red)

has_red = red == 1.0
print(has_red)

rows_with_red = colors[has_red]
print(rows_with_red)

print(colors.agg("mean"))

print(colors.drop("name", axis=1).agg("mean"))

print(colors.drop("name", axis=1)[colors["red"] == 1.0].agg("mean"))
