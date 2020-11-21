"""Test the various methods of writing a DataFrame to a file."""

import pandas as pd

df = pd.read_csv("df.csv")

df.to_csv("data.csv")
df.to_excel("data.xlsx")
df.to_stata("data.dta")