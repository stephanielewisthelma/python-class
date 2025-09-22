import pandas as pd


data = {
    "Name": ["john", "korede", "daniel"],
    "Age": [25, 30, 28],
    "City":["rivers","imo","lagos"]
}

df = pd.DataFrame(data)

print(df)


# data ={
#     "Name":["john","korede","daniel","korede","frank","david"],
#     "study hours":[5,3,3,4,6,7],
#     "score":[8,6,9,5,7,2],
#     "score":[80,60,92,55,88,72]
# }
# df = pd.DataFrame(data)

# print(df)