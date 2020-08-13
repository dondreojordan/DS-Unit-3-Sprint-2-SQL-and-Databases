import pandas as pd
import psycopg2
import sqlite3


"""change csv to sqlite"""
df = pd.read_csv("titanic.csv")
df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
              'Parents/Children Aboard', 'Fare']


"""
insert data into new table
"""
connection = sqlite3.connect('titanic.sqlite3')
df.to_sql('titanic_review', connection, index=False)
cursor = connection.cursor()
cursor.execute('SELECT * FROM review').fetchall()
print(df.shape)
print(df.head)
"""
Count how many rows you have
"""
query = "SELECT COUNT(*) FROM review"
print(cursor.execute(query).fetchall()[0][0])
"""
Connect to the elphant database
"""
dbname = 'vbmmjeoc'
user = 'vbmmjeoc'  # ElephantSQL happens to use same name for db and user
password = 'qiPPfJeCLmtX5-yUZcV27SmlTz75PQka'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
DB_FILEPATH = "titanic.sqlite3"
sl_conn = sqlite3.connect(DB_FILEPATH)
sl_curs = sl_conn.cursor()
"""
Query
"""
sl_curs.execute('PRAGMA table_info(review);')
sl_curs.fetchall()

# A bunch of integers, and a varchar
# We need to make a create statement for PostgreSQL that captures this
create_titanic_table = """
CREATE TABLE def (
  Survived INTEGER,
  Pclass INTEGER,
  Name VARCHAR(30),
  Sex TEXT,
  Age REAL,
  Siblings_Spouses_Aboard INTEGER,
  Parent_Childeren_Aboard INTEGER,
  Fare REAL
);
"""
for row in df:
    cursor.execute(
                """
                    INSERT INTO 
                        def (
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
    print(df)
# Execute the create table
pg_curs = pg_conn.cursor()
pg_curs.execute(create_titanic_table)
pg_conn.commit()
#pandas - to_records