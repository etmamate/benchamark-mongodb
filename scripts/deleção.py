import csv
import time
from pymongo import MongoClient


repeticoes = 1
start_total_tempo = time.time()
for i in range(repeticoes):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['movies']
    collection = db['movies']

    start_consulta1 = time.time()
    print("\nRemovendo filmes com popularidade menor que 20...")
    delete_low_popularity = collection.delete_many(
    {"popularity": {"$lt": 20}}
    )
    print(f"Filmes removidos: {delete_low_popularity.deleted_count}")
    end_consulta1 = time.time()
    total_consulta1 = end_consulta1 - start_consulta1

    start_consulta2 = time.time()
    print("\nRemovendo filmes com média de votos inferior a 4.5...")
    delete_low_rating = collection.delete_many(
    {"vote_average": {"$lt": 4.5}}
    )
    print(f"Filmes removidos: {delete_low_rating.deleted_count}")
    end_consulta2 =  time.time()

    total_consulta2 = end_consulta2 - start_consulta2

    # Salvar no CSV
    with open('resultados/results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Removendo filmes com popularidade menor que 20', total_consulta1])
        writer.writerow(['Removendo filmes com média de votos inferior a 4.5', total_consulta2])
        writer.writerow(['Média de Segundos para cada Consulta: ', (total_consulta1 + total_consulta2) / 2])

end_total_tempo = time.time()

total = end_total_tempo - start_total_tempo
print(f"Média de segundos {total / 2}")