import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

#the csv module has reader function that allows specify limiter on file
csv_file = csv.reader(open_file, delimiter = ",")
#way that columns are separated are through comma

#reads the header, then from here cursor is past the first row in csv file, but not in regular
header_row = next(csv_file)

#header_row is printed as: ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
#looking at index value and what index is assoc. w data item

#the enumerate() function returns both the index of each item and the value
#of each item as you loop through a list 
#enumerator function returns tuples that you can split into two varaibles

#splits the index and column_header as a tuple
#csv reader reads line by line (AKA row by row)**************
#this for loop goes over just header, enumerates give index and value
for index, column_header in enumerate(header_row):
    print("Index:", index, 'Column Name:', column_header)

#if just want highest temp, which is index 5 
highs = []

for row in csv_file:
    highs.append(int(row[5])) #gives high temps for file, index values tell column

print(highs) 
#^ checks

#plot highs on chart

import matplotlib.pyplot as plt

plt.plot(highs, c="red")  #c = red is just choosing color

plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("", fontsize = 16)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis ="both", which = "major", labelsize=16) #customizing tick marks

plt.show() #visualizes chart