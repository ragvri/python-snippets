import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')


#dataframe is like a spreadsheet. It can take multiple form but generally needs to be a dataset that can form rows and cols

web_stats={'Day':[1,2,3,4,5,6],
           'Visitors':[43,5,4,6,5,6],
           'Bounce Rate':[4,5,6,3,44,8]}



df=pd.DataFrame(web_stats) #creating a data frame which is like an excel spreadsheet



print(df)  # we get an index starting from 0 on printing

print(df.head()) #df.head() prints first five rows
print(df.tail()) #prints last 5 rows

print(df.tail(2)) # prints last 2 rows


#set an index to the df like in this example day can be the index
#df.set_index('Day')
# however this returns a new data frame. So
#df=df.set_index('Day')

#another method
df.set_index('Day',inplace=True)

#to reference a specific col
print(df['Visitors']) # works like a dict
# can also do
print(df.Visitors) #same thing

print(df[['Visitors','Bounce Rate']]) #get 2 columns

print(df.Visitors.tolist()) # gives a list

# to get lists of 2 cols print(df[['Visitors','Bounce Rate']].tolist()) won't work
# so use numpy array

print(np.array(df[['Bounce Rate','Visitors']]))



