from pymongo import MongoClient
import pandas as pd

df = pd.read_csv('tmdb_top_movies.csv')
client = MongoClient('mongodb://localhost:27017/')
db = client ['benchamarknosql']
colecao = db['filmes']


#Inserção em massa
# colecao.insert_many(df.to_dict('records'))
print("Inserção concluída")

import time

#Consulta simples
inicio = time.time()
resultado = colecao.find_one({"title": "Tokyo Story"})
fim = time.time()
print(resultado, f"Tempo: {fim - inicio:.4f} s")