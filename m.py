import pandas as pd
import numpy as np

df = pd.read_csv("data_science_job.csv")
# df.head()
# print(df.head())
print(df.isnull().mean()*100)
