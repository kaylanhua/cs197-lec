import pandas as pd
import numpy as np

df = pd.read_csv('predictions.csv')

df["model_correct"] = np.where(df['labels'] == df["model"], True, False)
df["path_correct"] = np.where(df['labels'] == df["path"], True, False)

print(df.head())

df["B"] = np.where((df["model_correct"] == False) & (df["path_correct"] == True), True, False)
df["C"] = np.where((df["model_correct"] == True) & (df["path_correct"] == False), True, False)

# df1 = df[(df["model_correct"] == False) & (df["path_correct"] == True)]

print(df.head())

B = df['B'].sum()
C = df['C'].sum()

print(B)
print(C)



