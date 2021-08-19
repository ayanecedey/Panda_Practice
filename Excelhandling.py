import pandas as pd

df1 = pd.read_excel("D://Panda_Practice//Testdata//Sample.xls", "Sheet1")
df2 = pd.read_excel("D://Panda_Practice//Testdata//Sample.xls", "Sheet2")
#print(df1.compare(df2))
#print(df1.equals(df2))
dfnw1=df1.iloc[0:4, 0] #row range, col range
dfnw2=df1.iloc[0:4, 1]
nwdf=pd.concat([dfnw1, dfnw2], axis=1)
#print(nwdf)
dfnw3=df1.iloc[0:2, 0:2] #row range, col range
dfnw4=df1.iloc[3:5, 0:2]
nwdf2=pd.concat([dfnw3, dfnw4], axis=0)
#print(nwdf2.sort_values(by=['Country'], ascending=True))
print(df1.nlargest(1, 'Gross Sales', keep='all'))


'''
#nwdf.to_excel("D://Panda_Practice//Testdata//Writeexcel.xlsx", index=False, sheet_name="data")
#nwdf.to_excel("D://Panda_Practice//Testdata//Writeexcel.xlsx", startrow=1, index=False, sheet_name="data")
print("Updated Done")
'''
'''
writer = pd.ExcelWriter("D://Panda_Practice//Testdata//Writeexcel.xlsx")
nwdf.to_excel(writer, index=False)
nwdf.to_excel(writer, startrow=len(nwdf)+1, header=False, index=False)
writer.save()
print("Updated Done")
'''