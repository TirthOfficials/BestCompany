''' Code Written by Tirth Patel
    Date: 02-Feb-2022
'''

import pandas as pd

data = pd.read_csv("Data2.csv")
print("-----------------------------------------THE UNSORTED DATA-----------------------------------------")
print("")
print(data)
data["ROCE Rank"] = data["ROCE"].rank(ascending=False)

data

data.sort_values("ROCE", ascending=False,inplace = True)
print("")
print("-----------------------------------------THE SORTED DATA-----------------------------------------")
print("")

print(data.iloc[:])
print("")
print("THE BEST COMPANY ACCORDING TO ROCE IS ",data.iloc[0:1,1:2])
print(data.iloc[0:1,9:14])
print("")

data["Sales Rank"] = data["Net_Sales"].rank(ascending=False)



data.sort_values("Net_Sales", ascending=False,inplace = True)


print("")
print("THE BEST COMPANY ACCORDING TO SALES GROWTH IS ",data.iloc[0:1,1:2])
print(data.iloc[0:1,9:14])
print("")
data["Income Rank"] = data["Net_Profit"].rank(ascending=False)



data.sort_values("Net_Profit", ascending=False,inplace = True)


print("")
print("THE BEST COMPANY ACCORDING TO INCOME GROWTH IS ",data.iloc[0:1,1:2])
print(data.iloc[0:1,9:14])
print("")
data["Debt/Equity Rank"] = data["Debt/Equity_Ratio"].rank(ascending=False)



data.sort_values("Debt/Equity_Ratio", ascending=False,inplace = True)


print("")
print("THE BEST COMPANY ACCORDING TO Debt/Equity Ratio IS ",data.iloc[0:1,1:2])
print(data.iloc[0:1,9:14])





