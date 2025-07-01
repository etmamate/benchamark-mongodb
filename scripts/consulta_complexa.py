import csv
import time
from datetime import datetime
from pymongo import MongoClient

repeticoes = 1
start_total = time.time()
for i in range(repeticoes):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['movies']
    collection = db['movies']


    #Média de votos por década
    start_consulta1 = time.time()
    print("\nMédia de votos por década:")
    pipeline_decade = [
        {
            "$project": {
                "decade": {
                    "$subtract": [
                        "$year",
                        {"$mod": ["$year", 10]}
                    ]
                },
                "vote_average": 1
            }
        },
        {
            "$group": {
                "_id": "$decade",
                "avg_vote": {"$avg": "$vote_average"},
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    decade_avg = collection.aggregate(pipeline_decade)
    for result in decade_avg:
        print(f"Década {result['_id']}: Média {result['avg_vote']:.2f} ({result['count']} filmes)")

    end_consulta1 = time.time()

    #Filmes por década com média de avaliação e quantidade
    start_consulta2 = time.time()
    print("\nTop 5 anos com maior média de popularidade:")
    pipeline_popularity = [
        {
            "$group": {
                "_id": "$year",
                "avg_popularity": {"$avg": "$popularity"},
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"avg_popularity": -1}},
        {"$limit": 5}
    ]
    top_popularity = collection.aggregate(pipeline_popularity)
    for result in top_popularity:
        print(f"Ano {result['_id']}: Popularidade média {result['avg_popularity']:.2f} ({result['count']} filmes)")

    end_consulta2 = time.time()

    # Salvar no CSV
    with open('resultados/results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Consulta Complexa - Média de votos por década' , end_consulta1 - start_consulta1])
        writer.writerow(['Consulta Complexa - Top 5 anos com maior média de popularidade' , end_consulta2 - start_consulta2])


end_total = time.time()

tempo_total = end_total - start_total
print(f"Segundos totais: {tempo_total}")
print(f"Média total dos segundos: {tempo_total /2}")