"""Using the standard sqlite3 module:

Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
"""
import os
import sqlite3
import random
import pandas as pd

           
# df = pd.read_csv('buddymove_holidayiq.csv')
# print('Dataframe Shape:', df.shape)
# print(df.isnull().sum().sort_values(ascending=False))

# # DB_FILEPATH = "module1-introduction-to-sql/buddymove_holidayiq.csv"            
connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
# # print("CONNECTION:", connection)

# # Write records stored in DF
# df_to_sql = df.to_sql('review', connection)

cursor = connection.cursor()
# print("CURSOR:", cursor)

### Count how many rows you have? Hint: 249
query = """
        SELECT COUNT(*) 
        FROM review
        """
### How many users who reviewed at least 100 `Nature` in the category 
### also reviewed at least 100 in the `Shopping` category?
query2 = """
        SELECT COUNT(Nature) 
        FROM review
        WHERE Nature > 100
        AND Shopping > 100
        """


result = cursor.execute(query).fetchall()
print("RESULT of Query:", result)  #> returns cursor objects w/o results (need to fetch)

result2 = cursor.execute(query2).fetchall()
print("RESULT of Query 2:", result2)

# No complaints - which means they're all the same!
# Closing out cursor/connection to wrap up
cursor.close()
connection.close()