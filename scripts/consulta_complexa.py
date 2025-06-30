import csv
import time
from datetime import datetime
from pymongo import MongoClient

for i in range(10):
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