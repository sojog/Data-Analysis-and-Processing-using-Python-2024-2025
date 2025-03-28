from django.test import TestCase

# Create your tests here.

# print(ord('A')) # 65
# print(ord('B'))
# print(ord('E'))
# print(ord('Z'))

# print(ord('a'))
# print(ord('z'))


# # 65..90
# # 97..122

# print(chr(65))
# print(chr(122))


# for i in range(ord('A'), ord('Z')+1):
#     print(chr(i))



import pandas as pd


with open("parole.csv", "w") as fwriter:
    fwriter.write("parole")

df = pd.read_csv("parole.csv")

print(df)
df.to_json("parole.json")

