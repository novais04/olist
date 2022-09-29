
import os
import pandas as pd
import sqlalchemy

user = 'bf30ecb3791b07' # login
psw = 'b9883e7d' # senha
database = 'heroku_b7f3e56c278b1b6'
host = 'us-cdbr-east-06.cleardb.net' # ip/host/dns
port = '3306' # porta

str_conection = 'mysql+pymysql://{user}:{psw}@{host}:{port}/{database}'

# Os endereços de nosso prjeto e sub pastas
BASE_DIR = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
    

# Encontrando os arquivo de dados
file_names = [i for i in os.listdir(DATA_DIR) if i.endswith(".csv")]

# Arbindo conexão com o banco...
str_conection = str_conection.format(user=user, psw=psw, host=host, port=port, database=database)
connection = sqlalchemy.create_engine( str_conection)

# Para cada arquivo realiza a inserção dos dados no banco
for i in file_names:
    print(i)
    df_temp = pd.read_csv(os.path.join(DATA_DIR, i))
    table_name = "tb_" + i.strip(".csv").replace("olist_","").replace("_dataset","")
    df_temp.to_sql(table_name,con=connection,if_exists='replace',index= False)
    
                          


