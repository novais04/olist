import os
import pandas as pd
import sqlalchemy

user = 'root' # login
psw = 'Dantefn_2010' # senha
database = 'olist'
host = 'localhost' # ip/host/dns
port = '3306' # porta

str_conection = 'mysql+pymysql://{user}:{psw}@{host}:{port}/{database}'

# Os endereços de nosso prjeto e sub pastas
BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
    
# Encontrando os arquivo de dados
file_names = [i for i in os.listdir(DATA_DIR) if i.endswith(".csv")]

# Arbindo conexão com o banco...
str_conection = str_conection.format(user =user, psw=psw, host=host, port=port, database=database)
connection = sqlalchemy.create_engine( str_conection)

# inclundo as tabelas no banco de dados
for i in file_names:
    print(i)
    df_temp = pd.read_csv(os.path.join(DATA_DIR, i))
    table_name = "tb_" + i.strip(".csv").replace("olist_","").replace("_dataset","")
    df_temp.to_sql(table_name,con=connection,if_exists='replace',index= False)


