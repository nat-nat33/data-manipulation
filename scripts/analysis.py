import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

#Reading the dataset in a dataframe using Pandas
df = pd.read_csv("./data/mock_app_data.csv") 

#returns number of rows
print("num of rows: ", len(df.index))

#returns number of columns
print("num of columns: ", len(df. columns))

#returns first 10 rows with header
df.head(10)

# basic description of the data
df.describe()

# count for variations in gender that have values
df['gender'].value_counts()