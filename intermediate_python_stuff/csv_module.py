# read a csv file

import csv  # csv means comma separated in delimiter

colors = []
dates = []
with open('eg.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')
    # print(readcsv)
    for row in readcsv:
        print(row)
        color = row[3]
        date = row[0]
        colors.append(color)
        dates.append(date)

whatcolor = input('What is the color you want to know the date of')
getcolor = dates[colors.index(whatcolor)]
print('the date of', whatcolor, 'is', getcolor)
