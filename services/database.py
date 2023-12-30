import pyodbc

server = 'dcsantosserver.database.windows.net'
database = 'bdsantos'
username = 'admserver'
password = 'bradock@13'
driver= '{ODBC Driver 18 for SQL Server}'
con = 'Yes'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()