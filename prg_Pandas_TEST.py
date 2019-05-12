import pandas as pd

df = pd.read_csv('D:\\Rajendra_2019\\Python_docs\\Sample_Stock-Pandas.csv')

# print("Showing the DATA(START)")
# print(df)
# print("Showing the DATA(END)")



# print("Show Keys[START")
#
# print(df.keys())
#
# print("Show Keys[END")



# maxclose = df[‘Close].max()
# print (maxtemp)
#
# df[‘EST’][df[‘Events’]==’Rain’]
#
# df.fillna(0,inplace=True)

#df[‘WindspeedMPH’].mean()

print("Export To Excel :  ")
df.to_excel('D:\\Rajendra_2019\\Python_docs\\Pandas_Dataset.xls', index=False)
print('Export to Excel (Completed)')

print("Show Data Types (START)")

print(df.dtypes)


print("Show Data Types (END)")


maxStockClose = df["Close"].max()
print ("Stock Max Closing : " , maxStockClose)
#
avgclose = df["Close"].mean()
#print (avgclose)
print ("Stock Average Closing : " , avgclose)


#print(df["Volume"])

volume_max = df["Volume"].max()
volume_min = df["Volume"].min()


print ("Max Volume : ", volume_max)
print ("Min Volume : ", volume_min)


# Showing the Group By data

print("Group By data  (START)")

#groupby_data_Stock = df.groupby('Date').aggregate(sum)

groupby_data_Stock = df.groupby(['Close','Volume']).sum()


print(groupby_data_Stock)

print("Group By data  (END)")



print("Filtering the data based on WHERE ")
print("====================================")
# filter1 = df["Close"] > 260
# filter2 = df["Volume"] > 100000
#
# df.where(filter1 & filter2 , inplace = True)
# print(df)

print("====================================")


#
# print(df.[Volume]).max()
# print(df.[Volume]).min()
#
#
# print(df.head(2))


