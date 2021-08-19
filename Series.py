import pandas as pd

#print(pd.__version__)

#Series used for 1 dimensional array or like column in table#
#List
a=[1,4,8]
myvar=pd.Series(a)
#print(myvar[0])
myvarnw=pd.Series(a, index=["1st", "2nd", "3rd"])
#print(myvarnw["1st"])

#Dictionary
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
myvardic=pd.Series(calories)
#print(myvardic["day1"], myvardic[1])
print(myvardic)
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.#

