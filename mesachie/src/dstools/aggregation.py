import pandas as pd

example = pd.DataFrame(
    data=[[1, 2, 3], [10, 20, 30], [100, 200, 300]],
    columns=["left", "middle", "right"],
)
print(example)
print(example["middle"] + example["right"])
print(7 * example["left"])
print(example.agg("sum"))
print(example.agg(["sum", "mean"]))
