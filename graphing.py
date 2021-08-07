import pandas as pd
import matplotlib.pyplot as plt

covidData = pd.read_excel('covidData.xlsx')

list_dates = (list(covidData.columns.values[1:518]))

list_names = (list(covidData['County Name'].loc[0:255]))

# gives a list of case nums for user given county
def dataFunc():
	county_name  = input("What County's data do you want to see? ")
	for i in range(len(list_names)):
		if list_names[i]  == county_name:
			#print(list(covidData[list_dates].loc[i]))
			return(list(covidData[list_dates].loc[i]))
			break
	else:
		print('You have not entered a valid County name.')

# line graph using matplotlib for the given data
Date = list_dates
Number_of_Covid19_Cases = dataFunc()

plt.plot(Date, Number_of_Covid19_Cases, color='magenta')
plt.title('Covid 19 Cases in a County', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Number of Covid 19 Cases', fontsize=16)

plt.show()
 
