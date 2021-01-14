""" Without the use of Pandas. Works"""


import psycopg2
from csv import DictReader
import csv

# DictReader : 
# Looks similar to sqlite3, but needs auth/host info to connect
# Note - this is sensitive info (particularly password)

dbname = 'sqgkwexl'
user = 'sqgkwexl'  # ElephantSQL happens to use same name for db and user
password = 'zE0CXOxmT67Awf1WbLSmTzJ_bypd8aFv'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute("""
CREATE TYPE SEX_SEX AS ENUM ('male', 'female');

CREATE TABLE abc (
  id SERIAL PRIMARY KEY,
  survived BOOLEAN NOT NULL, 
  pclass INTEGER NOT NULL,
  name varchar(255) NOT NULL,
  sex SEX_SEX NOT NULL,
  age DECIMAL NOT NULL, 
  siblings_spouse_count INTEGER NOT NULL,
  parents_children_count INTEGER NOT NULL,
  fare DECIMAL NOT NULL
);
""")
# NOTE - these types are PostgreSQL specific. This won't work in SQLite!

# iterate over each line as a ordered dictionary and print only few column by column name
# https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/ (Documentation)
# with open('titanic.csv', 'r') as read_obj:
#     csv_dict_reader = DictReader(read_obj)
#     for row in csv_dict_reader:
#         pg_curs.execute(
with open('titanic.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
          pg_curs.execute(
            """
                INSERT INTO 
                    abc (
                        survived, 
                        name, 
                        pclass, 
                        sex, 
                        age, 
                        siblings_spouse_count, 
                        parents_children_count, 
                        fare
                    ) 
                VALUES 
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s   
                    );
            """,
            (
                row['Survived'], 
                row['Name'], 
                row['Pclass'], 
                row['Sex'], 
                row['Age'], 
                row['Siblings/Spouses Aboard'],
                row['Parents/Children Aboard'],
                row['Fare']
            )
        )



pg_conn.commit()  # "Save" by committing
pg_curs.close()
pg_conn.close()  # If we were really done



