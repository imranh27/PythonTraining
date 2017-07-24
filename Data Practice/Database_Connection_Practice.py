



#import database libraries
from sqlalchemy import create_engine
import pyodbc
import urllib

#import pandas
import pandas as pd

#define database connection parameters
server = 'SQLPMSDBX03'
database = 'BD_Aderant_RS_Data'
username = 'reporter'
password = 'report'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

params = urllib.quote_plus('DRIVER={SQL Server Native Client 10.0};SERVER='+server+';DATABASE='+database+';UID='+username+'+;PWD='+password)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

#initialise engine
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
#engine = create_engine(cnxn)
con = engine.connect()

#query
rs = con.execute("SELECT EMPLOYEE_CODE FROM BD_REPS_NOMINAL_STAFF_GROUPS")

#populate dataframe
df = pd.DataFrame(rs.fetchall())

#close connection
con.close()


#inspect dataframe
df.head()






