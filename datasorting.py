import pandas as pd
import matplotlib.pyplot as plt 

#load and visualise dataset 
data = pd.read_csv ("car_price_prediction_.csv")
print(data.head())

#check for missing values, categorical and numerical 
for column in data.columns:
    if data[column].isnull().any():
        if data[column].dtype == 'object':
            #replace cat. data with mode
            data[column].fillna(data[column].mode()[0], inplace = True)
        else:
            #replace num. data with mean 
            data[column].fillna(data[column].mean(), inplace = True)
    print(f"{column}: {data[column].isnull().sum()} missing values")

X = data.iloc[:,: -1]
y = data.iloc[:, -1]

