import pandas as pd

covidData = pd.read_excel('covidData.xlsx')
print(covidData.columns)

list_dates = ######
for i in :
	print(covidData['Cases 03-04-2020'].loc[0])

list_dates = (list(covidData.columns.values[1:518]))
print(list_dates)

list_names = (list(covidData['County Name'].loc[0:255]))
print(list_names)

#for i in range(len(list_dates)):
print(list(covidData[list_dates].loc[0])) #gives Anderson case nums 
print(list(covidData[list_dates].loc[1])) #gives Andrews data
