import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('dataset.csv')

# take a peek at the data
# print("Shape of the dataset: ", df.shape)
# print("First 5 rows of the dataset:\n", df.head())
# print("Dataset Info:\n  ", df.info())
# print("Statistical Summary:\n", df.describe())

# Check for missing values
# print("Missing values in each column:\n", df.isnull().sum())

# handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)
# print("Missing values in each column:\n", df.isnull().sum())

# Count for those who survived vs those who did not
print("Survival Counts:\n", df['Survived'].value_counts())

# visualuzations
sns.countplot(x='Survived', data=df)
plt.title('Survival Counts(0 = Died, 1 = Survived)')
plt.show()


sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival Counts by Gender (0 = Died, 1 = Survived)')
plt.show()


sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.show()


sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age Distribution by Passenger Class')
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')