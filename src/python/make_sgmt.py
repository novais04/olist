import os
import sqlalchemy
import pandas as pd
import argparse

# Os endereços de nosso prjeto e sub pastas
BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SQL_DIR = os.path.join(BASE_DIR, 'src','sql')

with open(os.path.join(SQL_DIR, 'segmentos.sql')) as query_file:
    query= query_file.read()
    
# Arbindo conexão com o banco...
str_conection = 'sqlite:///{path}'
str_conection = str_conection.format(path=os.path.join(DATA_DIR,'olist.db'))
connection = sqlalchemy.create_engine( str_conection)

df = pd.read_sql_query(query, connection)
print(df)