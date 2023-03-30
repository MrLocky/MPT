import pyodbc

class DataBaseClass:
    def BaseMethod(DB_string):
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
            "Server=LAPTOP-JI7GCH89\DANILA;"
            "Database=Prac3;"
            "Trusted_Connection=yes;")
        cursor = cnxn.cursor()
        cursor.execute(DB_string)
        return cursor