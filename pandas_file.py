import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# data = {
#     "Name": ["john", "korede", "daniel"],
#     "Age": [25, 30, 28],
#     "City":["rivers","imo","lagos"]
# }

# df = pd.DataFrame(data)

# print(df)


# data ={
#     "Name":["john","korede","daniel","korede","frank","david"],
#     "study hours":[5,3,3,4,6,7],
#     "score":[8,6,9,5,7,2],
#     "score":[80,60,92,55,88,72]
# }
# df = pd.DataFrame(data)

# print(df)

data = pd.read_csv("titanic.csv")
print ("shape of dataset:",data.shape)
print ("\nfirst five rows \n:",data.head)
print ("\ndataset info: \n")
print (data.info())
print("\n summary statistics (numeric column)\n",data.descripe())

# missing value


# print(data.head())
# print(data.tail())
# print(data["Age"].fillna(data["Age"].median(),inplace = True))
# print (data["Age"].fillna(data["Age"].median()))
# print (data.drop())

# data = pd.read_csv("student_data.csv")
# print(data.head())
# print(data.tail())
# print(data.isnull().sum())

# regression and classification

