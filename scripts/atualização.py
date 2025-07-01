import time
from pymongo import MongoClient
import csv

repeticoes = 1
start_tempo_total = time.time()
for i in range(repeticoes):
    # Conexão com o MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['movies']
    collection = db['movies']

    start_consulta1 = time.time()
    print("\nAtualizando notas (+0.2) para filmes com mais de 10.000 votos...")
    update_high_votes = collection.update_many(
        {"vote_count": {"$gt": 10000}},
        {"$inc": {"vote_average": 0.2}}
    )
    print(f"Filmes atualizados: {update_high_votes.modified_count}")
    end_consulta1 = time.time()

    start_consulta2 = time.time()
    print("\nAumentando popularidade de filmes lançados em 2020...")
    update_2020 = collection.update_many(
        {"year": 2020},
        {"$mul": {"popularity": 1.5}}  # Aumenta em 50%
    )
    print(f"Filmes de 2020 atualizados: {update_2020.modified_count}")
    end_consulta2 = time.time()

    # Registrar o tempo
    total_consulta1 = end_consulta1 - start_consulta1
    total_consulta2 = end_consulta2 - start_consulta2
    print(f"Tempo de atualização (título): {total_consulta1} segundos")
    print(f"Tempo de atualização (título): {total_consulta2} segundos")

    # Salvar no CSV
    with open('resultados/results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Atualização - Notas (+0.2) para filmes com mais de 10.000 votos', total_consulta1])
        writer.writerow(['Atualização - Aumentando popularidade de filmes lançados em 2020', total_consulta2])
        writer.writerow(['Média de Segundos para cada Consulta: ', (total_consulta1 + total_consulta2) / 2])
end_tempo_total = time.time()

total = end_tempo_total - start_tempo_total

print(f"Segundos: {total}")
print(f"Total")
print(f"Média de segundos: {total / repeticoes}")