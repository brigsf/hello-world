
#import datetime
#print("Hello, world!")
#x = datetime.datetime.now()
#print("Today is ", x)
#y = datetime.datetime
#print(y)


import pyodbc
import pandas as pd
# insert data from csv file into dataframe.
# working directory for csv file: type "pwd" in Azure Data Studio or Linux
# working directory in Windows c:\users\username

#df = pd.read_csv("c:\\user\\username\department.csv")
df = pd.read_csv("C:\\MyWorkfiles\\Python_practice\\department.csv")

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

server = 'bgsqlsvr1.database.windows.net' 
database = 'bgsqldb1' 
username = 'bgsqladmin' 
password = 'bgsqlpass1!' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
    
    cursor.execute("INSERT INTO DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)
    
    #cursor.execute("INSERT INTO DepartmentTest (DepartmentID,Name,GroupName) values(1,'Engineering','Research and Development')")
    
cnxn.commit()
cursor.close()
