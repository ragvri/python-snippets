# read a csv file

import csv  # csv means comma separated in delimiter

colors = []
dates = []
with open('eg.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')  # delimeter tells how the data is separated. here they are by commas
    # print(readcsv)
    for row in readcsv:
        print(row)
        color = row[3]
        date = row[0]
        colors.append(color)
        dates.append(date)
try:
    whatcolor = input('What is the color you want to know the date of')
    getcolor = dates[colors.index(whatcolor)]
    print('the date of', whatcolor, 'is', getcolor)

# if anywhere in try there is error except will run
except Exception as e:  # saves the exception to variable e
    print(e)

print('''
To make
a
multiline print,
do as in comments

''')
