
#we hard coded indexes corresponding to TMIN and TMAX
#use header row to determine inedexes for these values so that program can work for both sitka and death valley
#use station name to auto generate appropriate title
#create 2 sub plot graphs in one visualization so can compare sitka and death valley
#matplotlib pyplot API has convenience function has convenience function called subplots() which acts as utility wrapper and helps create common layout of subplots, including the enclosing figure object, in singel tcall
# fig, ax = plt.subplots(2,2) creates a visualization w 2 charts on it
def main():
    import csv
    from matplotlib import pyplot as plt
    from datetime import datetime

    filename = open ('sitka_weather_2018_simple.csv','r')
    place_name =''


    #ask about this loop in class, believe it goes through each open file
    reader = csv.reader(filename, delimiter= ",")
    header_row = next(reader) #moves cursor past first line in text file, but header_file is the first line

    print(header_row)
    #now going to make auto indexes
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    #get dates, highs, and lows from this file
    dates, highs, lows = [], [], []
    for row in reader:
    #automatically gets name of place from file
        if not place_name:
            place_name = str(row[name_index])
            print(place_name)
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            converted_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        except ValueError:
            #exception if there is a value error
            #will print out whatever is missing
            #will give you last successful line
            print(f'Missing data for {converted_date}')
            #f is new string formatting technique, literal string interprelation, leading f and don't need commas anymore, incorporate vairables directly
        else:
            highs.append(high) #gives high temps for file
            dates.append(converted_date)
            lows.append(low)

    #lets start graphing the first subplot
    fig, a = plt.subplots(2,1)
    
    a[0].set_title(place_name)
    a[0].plot(dates, highs, c='red')
    a[0].plot(dates, lows, c='blue')
    a[0].fill_between (dates, highs, lows, facecolor = 'blue', alpha= 0.1)

#now we get our death valley auto index info and plot

    
    filename = open('death_valley_2018_simple.csv', 'r')
    place_name2 =''


    #ask about this loop in class, believe it goes through each open file
    reader = csv.reader(filename, delimiter= ",")
    header_row = next(reader) #moves cursor past first line in text file, but header_file is the first line

    print(header_row)
    #now going to make auto indexes
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    #get dates, highs, and lows from this file
    dates, highs, lows = [], [], []
    for row in reader:
    #automatically gets name of place (death valley) from file
        if not place_name2:
            place_name2 = str(row[name_index])
            print(place_name2)
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            converted_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        except ValueError:
            #exception if there is a value error
            #will print out whatever is missing
            #will give you last successful line
            print(f'Missing data for {converted_date}')
            #f is new string formatting technique, literal string interprelation, leading f and don't need commas anymore, incorporate vairables directly
        else:
            highs.append(high) #gives high temps for file
            dates.append(converted_date)
            lows.append(low)
    #now lets graph second subplot for death valley weather
    a[1].set_title(place_name2)
    a[1].plot(dates, highs, c='red')
    a[1].plot(dates, lows, c='blue')
    a[1].fill_between(dates, highs, lows, facecolor ='blue', alpha=0.1)

    #format big plot overall
    fig.suptitle(f'Temperature Comparison Between {place_name} and {place_name2}')
    plt.xlabel("", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)
    fig.autofmt_xdate
    #now for the graph to go!
    plt.show()


    #fig.suptitle(f'Temperature comp between {place_name1} and {place_name2}')
main()
        