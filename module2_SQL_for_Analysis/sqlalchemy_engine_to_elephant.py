import pandas as pd
from sqlalchemy import create_engine  # pip install First


df = pd.read_csv('titanic.csv')
engine = create_engine('postgres://sqgkwexl:zE0CXOxmT67Awf1WbLSmTzJ_bypd8aFv@isilo.db.elephantsql.com:5432/sqgkwexl')
df.to_sql('titanic', con=engine) # Take a look at the formatting options
