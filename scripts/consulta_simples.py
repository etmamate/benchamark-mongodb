import csv
import time
from pymongo import MongoClient

for i in range(10):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['movies']
    collection = db['movies']

    # Consulta simples: buscar filme por título
    start_time = time.time()
    result = collection.find_one({"title": "Inception"})  # Substitua pelo título real do dataset
    print(result)
    end_time = time.time()
    print(f"Tempo de consulta simples (título): {end_time - start_time} segundos")

    # Salvar no CSV
    with open('resultados/results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Consulta Simples - Titulo', end_time - start_time])