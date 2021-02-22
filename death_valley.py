#handle error checking using try and except
#change file name to use death valley data

#you have to look like death valley file and see if file is different, make the changes 
#auto indexing on assignment, should know how to extract from file, enumerate allows su to figure out what index has what value
#death valley indexes are different
from datetime import datetime  #so that you can use striptime

import csv
#cvs is a special reader

open_file = open("death_valley_2018_simple.csv", "r") #this is entire year instead of previous file just had month

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
highs = []
lows = []

#when you change indexes for death valley, you get value error. Line 50 has data missing in text file like real world
#use try and except method to fix value error problem

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        #exception if there is a value error
        #will print out whatever is missing
        #will give you last successful line
        print(f'Missing data for {converted_date}')
        #f is new string formatting technique, literal string interprelation, leading f and don't need commas anymore, incorporate vairables directly
    else:
        highs.append(int(row[4])) #gives high temps for file
        dates.append(converted_date)
        lows.append(int(row[5]))


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

