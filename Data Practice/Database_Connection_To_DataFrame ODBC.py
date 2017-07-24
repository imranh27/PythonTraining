#The following will import data from a query and put the data in to a dataframe

#imports
#import pyodbc
import pandas as pd
from sqlalchemy import create_engine

#define query
all_staff_all_time_sql = 'SELECT TK_CODE, TK_NAME, ' \
                         'TIME_CHRG_PRD, TIME_CHRG_PRD_BUDGET, ' \
                         'TIME_NCHRG_PRD ' \
                         'FROM BD_ADEXP_DW..VW_BD_REPS_STAFF_ALLTIME'

#connect to database
engine = create_engine("mssql+pyodbc://SQLPMSDBX03")
con = engine.connect();

rs = con.execute(all_staff_all_time_sql)

#populate dataframe
df = pd.DataFrame(rs.fetchall())

#add column headers
df.columns = rs.keys()

#close connection
con.close()

#reformat data columns as floats
df['TIME_CHRG_PRD'] = df['TIME_CHRG_PRD'].astype(float)
df['TIME_CHRG_PRD_BUDGET'] = df['TIME_CHRG_PRD_BUDGET'].astype(float)
df['TIME_NCHRG_PRD'] = df['TIME_NCHRG_PRD'].astype(float)

#inspect dataframe
print(df.head())
print(df.info())
#print(df.describe())

#write to file
out_csv = 'Data_Frame.csv'
df.to_csv(out_csv)




