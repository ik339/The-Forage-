   #import libraries.
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

   #read file.
path = r"C:\Users\ikors\.spyder-py3\Online_Retail.xlsx"
data = pd.read_excel(path) 

   #all columns displayed(small screen). 
pd.set_option("display.max.columns", None) 

   #exploratative analysis.
print(type(data))
print(data.head(2))
print(data.info()) 
print(data.shape) # 541 909 rows.

   #drop irrelevant columns.
data2 = data.drop('Description', axis=1)

   #drop CustomerID column.
data2.drop('CustomerID', axis=1, inplace = True)

   #drop and duplicate rows.
data2.drop_duplicates(inplace=True)

   #heatmap - visualise null values.
sns.heatmap(data2.isnull()) 

   #check again.
print(data2.shape) #now 536 639

   #creating commands in the task. 
data2.drop(data2[data2['Quantity'] < 1].index, inplace=True)
data2.drop(data2[data2['UnitPrice'] < 0].index, inplace=True)

   #check again.
print(data2.describe())
print(data2.shape) #526 050

     #multiply quantity + unit price columns to create a new column = revenue.
data2['Revenue']=data2['Quantity']*data2['UnitPrice']

   #turn the invoice date column to date-time format.
import datetime  
data2['InvoiceDate']=pd.to_datetime(data2['InvoiceDate']) 

    #extract 2011 date only into new data frame.
df_2011 = data2[data2['InvoiceDate'].dt.year == 2011]
df_2011.info() 

   #new column for the month.
df_2011['Month']=df_2011['InvoiceDate'].dt.month #1 df-2011 adds a col.

   # groupby month + revenue.
group_df = df_2011.groupby('Month')['Revenue'].sum()
group_df.head(3)
print(type(group_df))

   #convert series to a data frame.
conv_group_df = group_df.reset_index(inplace=True) #!!!!!!!!!!!!
conv_group_df.columns = ['Month', 'Revenue']
print(conv_group_df)

   #plot the timeseries graph.
plt.plot(conv_group_df['Month'],conv_group_df['Revenue'], linestyle = 'dotted')
plt.title('Monthly Revenue for 2011')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(conv_group_df['Month']) #added 12 ticks
plt.yticks(np.arange(400000,1600001,100000))
plt.show()
