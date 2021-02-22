#changing file to include all datat for yr 2018
#change title to daily high and low temps
#extract lwo temps and add from chart
#shade in area from highs and lows

from datetime import datetime  #so that you can use striptime

import csv
#cvs is a special reader

open_file = open("sitka_weather_2018_simple.csv", "r") #this is entire year instead of previous file just had month

#the csv module has reader function that allows specify limiter on file
csv_file = csv.reader(open_file, delimiter = ",")
#way that columns are separated are through comma

#skip header row, will skip any info from first header row
header_row = next(csv_file)

#looking at index value and what index is assoc. w data item

#the enumerate() function returns both the index of each item and the value
#of each item as you loop through a list 
#enumerator function returns tuples that you can split into two varaibles

#splits the index and column_header as a tuple
for index, column_header in enumerate(header_row):
    print("Index:", index, 'Column Name:', column_header)

#use striptime funciton to convert our str dates into dates
#as an example
"""
#striptime example
somedate = '2018-07-01'
converted_date = datetime.strptime(somedate, '%Y-%m-%d')
print(converted_date)
"""

#getting data list from file
dates= []
#if just want highest temp, which is index 5 
highs = []
lows = []

for row in csv_file:
    highs.append(int(row[5])) #gives high temps for file
    converted_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(converted_date)
    lows.append(int(row[6]))

#print(highs) 
#^ checks

#plot highs on chart

import matplotlib.pyplot as plt

fig=plt.figure() #so we can acess format part of figure, allows us to format so we call autoformat 
plt.plot(dates, highs, c="red")  #c = red is just choosing color
#dates are x coordinates, y are temperatures because exact same # dates and # y temperatures
#we want two lines, low line in blue
plt.plot(dates, lows, c = "blue")
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = .1) #alpha determines tint of blue, so we will get light blue here
#for every date, getting two values and it knows to shade in between the two values. Must always give x value and then two y values
#graph object is plt, when you write plt.plot that creates a new line
plt.title("Daily High and Low Temps-2018", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis ="both", labelsize=12) #customizing tick marks

fig.autofmt_xdate() #will automatically format x axis for dates that best fit figure to prevent overlapping

plt.show() #visualizes chart

#subplots allow you to format how many graphs can show up in one figure
#in assignment need to show difference btwn sitka and death valley ^

fig2, a = plt.subplots(2)
#need 2 subplots
# index 0 means frist subplot
a[0].plot(dates, highs, c = 'red') #plotting specific graph on figure
a[1].plot(dates, lows, c = 'blue') #plotting second subplot which is indicated by a[1]

plt.show()