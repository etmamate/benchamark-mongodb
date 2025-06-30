import time
from pymongo import MongoClient
import csv
from datetime import datetime
import os

# Verificar se o arquivo existe
file_path = 'datas/tmdb_top_movies.csv'  # Use / ou \\ ou raw string
if not os.path.exists(file_path):
    print(f"Erro: O arquivo {file_path} não foi encontrado. Verifique o caminho.")
    exit(1)

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['movies']
collection = db['movies']

# Inserção em massa
start_time = time.time()
documents = []
with open(file_path, 'r', encoding='utf-8') as f:  # Adicionei encoding='utf-8' para evitar problemas de codificação
    reader = csv.DictReader(f)
    for row in reader:
        row['id'] = int(row['id'])
        row['popularity'] = float(row['popularity'])
        row['vote_average'] = float(row['vote_average'])
        row['vote_count'] = int(row['vote_count'])
        row['release_date'] = datetime.strptime(row['release_date'], '%Y-%m-%d')
        documents.append(row)
collection.insert_many(documents)
end_time = time.time()
tempo_decorrido = end_time - start_time

print(f"Tempo de insercao: {tempo_decorrido} segundos")

with open('resultados/results.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([f'Insercao em Massa', {tempo_decorrido}])

import csv
import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['movies']
collection = db['movies']

# Consulta simples: buscar filme por título
start_time = time.time()
result = collection.find_one({"title": "Inception"})  # Substitua pelo título real do dataset
# print(result)
end_time = time.time()
print(f"Tempo de consulta simples (título): {end_time - start_time} segundos")

# Salvar no CSV
with open('resultados/results.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Consulta Simples - Titulo', end_time - start_time])

import csv
import time
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['movies']
collection = db['movies']

# Consulta complexa: média de votos por ano
pipeline = [
    {"$group": {"_id": {"$year": "$release_date"}, "avg_vote": {"$avg": "$vote_average"}}},
    {"$sort": {"_id": 1}}
]
start_time = time.time()
result = list(collection.aggregate(pipeline))
end_time = time.time()
print(result)
print(f"Tempo de consulta complexa (média por ano): {end_time - start_time} segundos")

# Salvar no CSV
with open('resultados/results.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Consulta Complexa - Média por Ano', end_time - start_time])