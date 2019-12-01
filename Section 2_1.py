import pandas as pd

### Series in lists
#
# ice_cream = ['vanilla','strawberry','chocolate','toffee']
# lottery = [4,8,16,32,64,128,256,512]
# registration = [True,False,False,True,True]

# print(pd.Series(ice_cream))
# print(pd.Series(lottery))
# print(pd.Series(registration))

### Series in Dictionary
#
# dict = {"Nikki":"678-538-8429",
#           "Taran":"678-207-9603"}
#
# s = pd.Series(dict)
# print(s.index)

prices = [5,8,9,6]
s = pd.Series(prices)
print(s)
print("Value of the sum is",s.sum())