import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('flights.csv', sep = ',')
names = pd.unique(data['CARGO'])

flights = []
prices  = []
weights  = []

for i in range(len(names)):
	frame = data.loc[data['CARGO'] == names[i]]
	flights.append(len(frame))
	prices.append(frame['PRICE'].sum())
	weights.append(frame['WEIGHT'].sum())
	
plot_data = pd.DataFrame({
	"flights_amount": flights,
	"sum_prices"    : prices,
	"sum_weight"    : weights
	},
	index = names)

plot_data.plot.pie(subplots=True, figsize=(11, 6))
plot_data.plot.pie(y = 'flights_amount')
plot_data.plot.pie(y = 'sum_prices')
plot_data.plot.pie(y = 'sum_weight')
plt.show()
