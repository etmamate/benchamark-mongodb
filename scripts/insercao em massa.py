import time
from pymongo import MongoClient
import csv
from datetime import datetime
import os

for i in range(10):
    
    file_path = 'datas/tmdb_top_movies.csv'  # Use / ou \\ ou raw string
    # Verificar se o arquivo existe
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