# working with pandas io all the data types that we can read in


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import  style
style.use('ggplot')

# we are using quandl which has free datasets
# link used for this https://www.quandl.com/data/ZILL/Z77006_MLP-Zillow-Home-Value-Index-ZIP-Median-List-Price-Houston

df = pd.read_csv('ZILL-Z77006_MLP.csv')  # since csv file .....for other input types search

df.set_index('Date', inplace=True)
# print(df.head())

df.to_csv('newcsv2.csv') # gives the data frame as output to new file

# df=pd.read_csv('newcsv2.csv')# reading from the recently made file#
# print(df) # again index changed :(

# better way
df = pd.read_csv('newcsv2.csv', index_col=0) # setting the index as col1 in the csv file
# print(df.head())

# rename a col
df.columns = ['Austin_hpi']  # remember setting a col as index removes its col status
# if multiple cols, then give the name in the list

# another way to rename
df.rename(columns={'Austin_hpi': 'Austin'}, inplace=True)  # orignal name of col and new name ...
# Can rename just one col

# if you don't want the headers in the file
df.to_csv('csv3.csv',header=False)
# what if we read from a file that does not have a header like csv3

df = pd.read_csv('csv3.csv', names=['Date', 'Austin_hpi'], index_col=0)
print(df.head())

# can use pandas to convert files!!
df.to_html('eg.html')  # creates a table in html

