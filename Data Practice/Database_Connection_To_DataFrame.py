#The following will import data from a query and put the data in to a dataframe

#imports
import pyodbc
import pandas as pd

#define connection parameters
server = 'SQLPMSDBX03'
database = 'BD_Aderant_RS_Data'
username = 'reporter'
password = 'report'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#define query
all_staff_all_time_sql = 'SELECT TK_CODE, TK_NAME, TIME_CHRG_PRD, TIME_CHRG_PRD_BUDGET, TIME_NCHRG_PRD FROM BD_ADEXP_DW..VW_BD_REPS_STAFF_ALLTIME'


#Sample select query
#cursor.execute(all_staff_all_time_sql)
#row = cursor.fetchall()
#while row:
#    print(row[0])
#    row = cursor.fetchall()

#alternative query
engine = create_engine("mssql+pyodbc://SQLPMSDBX03")
con = engine.connect()

rs = con.execute(all_staff_all_time_sql)

#populate dataframe
df = pd.DataFrame(rs.fetchall())

#close connection
con.close()

#inspect dataframe
df.head()



