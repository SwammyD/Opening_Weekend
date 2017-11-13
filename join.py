import pandas as pd

data = pd.read_csv("joined_25.csv")
data1 = pd.read_csv("new_out_with_finance_range_4000000_4587532.csv")
data2 = pd.read_csv("new_out_with_finance_range_3500000_4000000.csv")
data3 = pd.read_csv("new_out_with_finance_range_3200000_3500000.csv")
data4 = pd.read_csv("new_out_with_finance_range_3000000_3200000.csv")
#data5 = pd.read_csv("new_out_with_finance_range_3000000_3200000_2.csv")
data6 = pd.read_csv("new_out_with_finance_range_2500000_3000000.csv")
data7 = pd.read_csv("new_out_with_finance_range_2500000_3000000_2.csv")
data8 = pd.read_csv("new_out_with_finance_range_2000000_2500000.csv")
data9 = pd.read_csv("new_out_with_finance_range_1800000_2000000.csv")
data11 = pd.read_csv("new_out_with_finance_range_1600000_1800000.csv")
data12 = pd.read_csv("new_out_with_finance_range_1400000_1600000.csv")
data13 = pd.read_csv("new_out_with_finance_range_1200000_1400000.csv")
data14 = pd.read_csv("new_out_with_finance_range_1000000_1200000.csv")
data15 = pd.read_csv("new_out_with_finance_range_700000_1000000.csv")
data16 = pd.read_csv("new_out_with_finance_range_400000_700000.csv")
data17 = pd.read_csv("new_out_with_finance_range_200000_400000.csv")
data18 = pd.read_csv("new_out_with_finance_range_0_200000.csv")


#print(data)
#joined = pd.merge(data, ratings,  how='outer', on='tconst')
joined = pd.concat([data,data1,data2,data3,data4,data6,data7,data8,data9,data11,data12,data13,data14,data15,data16,data17,data18])

joinedwithoutdups = joined.drop_duplicates()

joinedwithoutdups.to_csv('joined_100.csv')

