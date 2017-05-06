import pandas as pd

# joining and merging data frames

df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])

# print(pd.merge(df1,df2, on='HPI'))         # duplicate info...ignores notion of index...on specifies on which thing
# are
#  we merging on
# if for example we have 2 tables: 1st has username and password as cols
# 2nd has username and nickname as cols... merging on username will give us a
# single table with the 2 cols appended
# print(pd.merge(df1,df2,on=['HPI',"Int_rate"]))

# join use
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)
# now they share an index but no cols..could also have merged on hpi

print(df1.join(df3))  # however again data repeats

df4 = pd.DataFrame({'Year': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]})

df5 = pd.DataFrame({'Year': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]})

print(pd.merge(df4, df5, on='Year', how='left'))  # how='Left' tells that the years of df4 (which is on left) need to be
# retained. If data for df5 is not available, then Nan showed
# putting how='outer' will join on the union of the keys. So in this case no data lost. If how='inner' then intersection


# as a thumb rule, use join when you care about the index, merge when you don't
