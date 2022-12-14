from ctypes import util
from email import parser
import os
from re import U
import sqlalchemy
import pandas as pd
import argparse
import datetime
import utils

# Os endereços de nosso prjeto e sub pastas
BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SQL_DIR = os.path.join(BASE_DIR, 'src','sql')

#parser de data para fazer a foto
parser = argparse.ArgumentParser()
parser.add_argument('--date-end', '-e',help='Data de fim da extração' ,default='2018-06-01')
args = parser.parse_args()

date_end = args.date_end
ano = int(date_end.split('-')[0]) -1
mes = int(date_end.split('-')[1])
date_init = f"{ano}-{mes}-01"

# importando query
query = utils.import_query(os.path.join(SQL_DIR, 'segmentos.sql'))
query = query.format( date_init = date_init, 
                       date_end = date_end )

#Abindo conexão com o banco...
conn = utils.connect_db()

create_query = f'''
CREATE TABLE tb_seller_sgmt AS 
{query};
'''

insert_query = f'''
DELETE FROM tb_seller_sgmt WHERE DT_SGMT = "{date_end}";
INSERT INTO tb_seller_sgmt  
{query};
'''

try:
    utils.execute_many_sql( create_query,conn )
except:
    utils.execute_many_sql(insert_query, conn, verbose=True )
          
          