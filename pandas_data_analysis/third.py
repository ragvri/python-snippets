import pandas as pd

#appending the dataframes

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])               # assigns index where the first index =2001 , second=2002 and so on
#print(df1)
df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])      # identical col with df1

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

concat=pd.concat([df1,df2,df3])
#print(concat) # not works properly

df4=df1.append(df3)
print(df4) # also not works properly

s=pd.Series(['30','32','32'] , index=['HPI','Int_rate','US_GDP_Thousands'])
df4=df1.append(s,ignore_index=True)