import pandas as pd

"""
    A B C
--+------
0 | 1 4 7
1 | 2 5 8
2 | 3 6 9
"""
df = pd.read_csv("drop.csv")

drop = df.drop(columns="A")
drop_axis = df.drop(["A"], axis=1)
drop_sugar = df.drop("A", axis="columns")

df.drop(columns=["B", "C"], inplace=True)

df.to_csv("drop.csv")