import pandas as pd
from sqlalchemy import create_engine

# read CSV file
column_names = ['name','birth', 'company']

df = pd.read_csv('/Users/cl.oliveira/Documents/SimpleETL/test.csv', header = None, names = column_names)
print(df)

df = pd.read_csv('/Users/cl.oliveira/Documents/SimpleETL/test.csv', header = 0)
print(df)


engine = create_engine('mysql://admin:admin@127.0.0.1:3306/db')
with engine.connect() as conn, conn.begin():
    df.to_sql('user', conn, if_exists='append', index=False)