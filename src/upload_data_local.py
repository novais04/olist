
import os
import pandas as pd
import sqlalchemy



str_conection = 'sqlite:///{path}'

# Os endereços de nosso prjeto e sub pastas
BASE_DIR = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
"""
print(f"Meu diretório de projeto é: {BASE_DIR}")
print(f"Meu diretório dos dados é: {DATA_DIR}")


file_names = os.listdir(DATA_DIR)
correct_files = []

#forma 1
for i in file_names:
    if i.endswith(".csv"):
        correct_files.append(i)
"""
    

# Encontrando os arquivo de dados
file_names = [i for i in os.listdir(DATA_DIR) if i.endswith(".csv")]

# Arbindo conexão com o banco...
str_conection = str_conection.format(path=os.path.join(DATA_DIR,'olist.db'))
connection = sqlalchemy.create_engine( str_conection)

# Para cada arquivo realiza a inserção dos dados no banco
for i in file_names:
    print(i)
    df_temp = pd.read_csv(os.path.join(DATA_DIR, i))
    table_name = "tb_" + i.strip(".csv").replace("olist_","").replace("_dataset","")
    df_temp.to_sql(table_name, connection)
                          


