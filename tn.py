import pandas as pd

covidData = pd.read_excel('covidData.xlsx')
#print(covidData.columns)

list_dates = (list(covidData.columns.values[1:518]))
#print(list_dates)

list_names = (list(covidData['County Name'].loc[0:255]))
#print(list_names)

#for i in range(len(list_names)):
#print(list(covidData[list_dates].loc[0])) #gives Anderson case nums 
#print(list(covidData[list_dates].loc[1])) #gives Andrews data

#if county_name.lower() == 'anderson':
	#print(list(covidData[list_dates].loc[0]))

county_name  = input("What County's data do you want to see? ")
for i in range(len(list_names)):
	if list_names[i]  == county_name:
		print(list(covidData[list_dates].loc[i]))
		break
else:
	print('You have not entered a valid County name.')
		 
