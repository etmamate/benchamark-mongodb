import csv
import random
import datetime

# Listas para gerar dados variados
categorias = [
    "Informática", "Eletrônicos", "Eletrodomésticos", "Móveis", 
    "Roupas", "Acessórios", "Livros", "Brinquedos", "Esportes"
]
marcas = ["Tech", "Super", "Pro", "Max", "Nova", "Eco", "Prime", "Ultra"]
tipos_produtos = [
    "Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", 
    "Televisão", "Geladeira", "Sofá", "Cadeira", "Camiseta", 
    "Tênis", "Mochila", "Livro", "Bola", "Raquete"
]

# Função para gerar nome de produto
def gerar_nome():
    marca = random.choice(marcas)
    tipo = random.choice(tipos_produtos)
    return f"{marca} {tipo}"

# Função para gerar preço
def gerar_preco(categoria):
    if categoria in ["Informática", "Eletrônicos"]:
        return round(random.uniform(500, 5000), 2)
    elif categoria == "Eletrodomésticos":
        return round(random.uniform(300, 3000), 2)
    elif categoria == "Móveis":
        return round(random.uniform(200, 2000), 2)
    elif categoria in ["Roupas", "Acessórios"]:
        return round(random.uniform(20, 200), 2)
    elif categoria in ["Livros", "Brinquedos", "Esportes"]:
        return round(random.uniform(10, 150), 2)
    return round(random.uniform(50, 1000), 2)

# Função para gerar data de compra aleatória
def gerar_data_compra():
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2025, 6, 28)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    data = start_date + datetime.timedelta(days=random_days)
    return data.strftime("%Y-%m-%d")

# Gerar 1000 registros
registros = []
for i in range(1, 1001):
    categoria = random.choice(categorias)
    preco = gerar_preco(categoria)
    quantidade = random.randint(1, 50)
    valor = round(preco * quantidade, 2)
    registro = {
        "id": i,
        "nome": gerar_nome(),
        "preco": preco,
        "categoria": categoria,
        "quantidade": quantidade,
        "valor": valor,
        "data_compra": gerar_data_compra()
    }
    registros.append(registro)

# Escrever para arquivo CSV
with open("produtos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "nome", "preco", "categoria", "quantidade", "valor", "data_compra"])
    writer.writeheader()
    writer.writerows(registros)

print("Arquivo produtos.csv gerado com 1000 registros.")