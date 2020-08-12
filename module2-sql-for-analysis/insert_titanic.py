import pandas as pd
import psycopg2
import sqlite3

conn = psycopg2.connect(
                        database="sqgkwexl", 
                        user="sqgkwexl", 
                        password="zE0CXOxmT67Awf1WbLSmTzJ_bypd8aFv", 
                        host = 'isilo.db.elephantsql.com'
                        )

# print(conn)

curs = conn.cursor()
# print(curs)

# Enumerate
# CREATE TYPE GENDER AS ENUM ('male', 'female');

a = curs.execute("""
DROP TABLE IF EXISTS PASSENGERS;

CREATE TYPE GENDER AS ENUM ('male', 'female');

CREATE TABLE "passengers" (
    Survived INT NOT NULL,
    Pclass INT NOT NULL,
    Name  VARCHAR(75) NOT NULL,
    Sex GENDER NOT NULL,
    Age REAL NOT NULL,
    Siblings_spouses_aboard INT NOT NULL, 
    Parents_children_aboard INT NOT NULL,
    Fare REAL NOT NULL
);
""")


df = pd.read_csv('titanic.csv')
for row in df:
    curs.execute(
                """
                    INSERT INTO 
                        passengers (
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
    
    
# df_to_sql = df.to_sql('review_titanic', conn)
# cursor = conn.cursor()
# ### Count how many rows you have? Hint: 249
# query = """
#         SELECT COUNT(*) 
#         FROM review_titanic
#         """
# ### How many users who reviewed at least 100 `Nature` in the category 
# ### also reviewed at least 100 in the `Shopping` category?
# query2 = """
#         SELECT COUNT(Survived) 
#         FROM review_titanic
#         WHERE Survived = 1
#         AND Fare > AVG(Fare)
#         AND Sex = 'female'
#         """
# cursor.execute(query)
# result = cursor.fetchall()
# print("RESULT of Query:", result)  #> returns cursor objects w/o results (need to fetch)

# cursor.execute(query2)
# result2 = cursor.fetchall()
# print("RESULT of Query 2:", result2)

# conn.commit()
# curs.close()
# conn.close()
