import pandas

df2 = pandas.read_json("supermarkets.json")

# print(df2)

df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)

# print(df3)

df4 = pandas.read_csv("supermarkets-commas.txt")

print(df4)