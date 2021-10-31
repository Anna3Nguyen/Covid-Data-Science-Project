import pandas as pd
import matplotlib.pyplot as plt

# reads excel file and returns county names and dates
def readFile():
	covidData = pd.read_excel('covidData.xlsx')
	list_dates = (list(covidData.columns.values[1:518]))
	list_names = (list(covidData['County Name'].loc[0:255]))
	return covidData, list_dates, list_names

# gives a list of case nums for user given county
def dataFunc(name, date, fileData):
        county_name  = input("What County's data do you want to see? ")
        for i in range(len(name)):
                if name[i] == county_name:
                        #print(list(fileData[date].loc[i]))
                        return(list(fileData[date].loc[i]))
                        break
        else:
                print('You have not entered a valid County name.')

# line graph using matplotlib for the given data
def graph(date, data):
	Day = date
	Number_of_Covid19_Cases = data
	plt.plot(Day, Number_of_Covid19_Cases, color='magenta')
	plt.title('Covid 19 Cases in a County', fontsize=20)
	plt.xlabel('Day', fontsize=16)
	plt.ylabel('Number of Covid 19 Cases', fontsize=16)
	plt.show()

def main():
	covidData, list_dates, list_names  = readFile()
	var = dataFunc(list_names, list_dates, covidData)
	graph(list_dates, var)

if __name__ == '__main__':
	main()

