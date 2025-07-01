import csv
import time
from pymongo import MongoClient

tempo_total_start = time.time()
repiticoes = 1
for i in range(repiticoes):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['movies']
    collection = db['movies']

    start_consulta1= time.time()
    print("\nFilmes com média de avaliação acima de 8.0:")
    high_rated = collection.find(
        {"vote_average": {"$gt": 8.0}}, 
        {"title": 1, "vote_average": 1, "_id": 0}
    ).limit(5)
    for movie in high_rated:
        print(movie)

    end_consulta1 = time.time()

    # Segundos totais da primeira consulta
    total_consulta1 = end_consulta1 - start_consulta1

    start_consulta2 = time.time()
    print("\nFilmes lançados depois de 2010:")

    recent_movies = collection.find(
        {"year": {"$gt": 2010}}, 
        {"title": 1, "year": 1, "_id": 0}
    ).limit(5)

    for movie in recent_movies:
        print(movie)


    #visualizar resultados
    # print(media_por_genero)
    end_consulta2 = time.time()
    total_consulta2 = end_consulta2 - start_consulta2



    
    print(f"Filmes com média de avaliação acima de 8.0: {total_consulta1} segundos")
    print(f"Filmes lançados depois de 2010: {total_consulta2} segundos")

    # Salvar no CSV 
    with open('resultados/results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Consulta Simples - Filmes com média de avaliação acima de 8.0 ', total_consulta1])
        writer.writerow(['Consulta Simples - Filmes lançados depois de 2010 ', total_consulta2])

tempo_total_end = time.time()
total_final = (tempo_total_end - tempo_total_start)
print(f"Segundos totais da operação: {total_final}")
print(f"Média dos segundos: {total_final / 2}")