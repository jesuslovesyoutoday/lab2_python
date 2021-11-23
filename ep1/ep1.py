import pandas as pd

print("#__________3_BIGGEST_PAYMENTS__________#\n")
data = pd.read_csv('transactions.csv', sep = ',')
frame1 = data.loc[data['STATUS'] == 'OK']
print(frame1.sort_values(by = 'SUM', ascending = False).head(3))

print("\n#_____ALL_PAYMENTS_TO_UMBRELLA,_INC____#\n")
frame2 = frame1.loc[data['CONTRACTOR'] == 'Umbrella, Inc']
print(frame2['SUM'].sum())
