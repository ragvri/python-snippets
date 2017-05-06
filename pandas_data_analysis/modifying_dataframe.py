import pandas as pd

HPI_data = pd.read_pickle('/home/raghav/Dropbox/coding/python/projects/data_analysis_HPI/states.pickle')

# print(HPI_data.head())

HPI_data['Tx2'] = HPI_data['TX'] * 2  # creates a new col where every entry is double the value in col of texas
print(HPI_data[['Tx2', 'TX']])  # prints out only two columns
