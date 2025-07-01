# 🎬 Análise de Dados de Filmes com MongoDB
#### Este projeto realiza análises em um conjunto de dados de filmes utilizando MongoDB, incluindo consultas simples e complexas, atualizações e operações de deleção. E comparando com banco de dados relacionais (MySQL).

### 📋 Tarefas Realizadas
🔍 Consultas Implementadas

#### Consultas Simples:

✅ Filmes com média de avaliação acima de 8.0

✅ Filmes lançados depois de 2010

#### Consultas Complexas:

✅ Média de votos por década

✅ Top 5 anos com maior média de popularidade

#### ✏️ Operações de Atualização
✅ Aumento em 0.2 da nota para filmes com mais de 10.000 votos

✅ Aumento da popularidade em 50% para filmes lançados em 2020

#### 🗑️ Operações de Deleção
✅ Remoção de filmes com popularidade menor que 20

✅ Remoção de filmes com média de votos inferior a 4.5

### 🛠️ Tecnologias Utilizadas
* Python 3.x
* MongoDB
* PyMongo (driver Python para MongoDB)
* Pandas (para carga inicial dos dados)

#### ⚙️ Configuração do Ambiente
* Pré-requisitos:
* MongoDB instalado e rodando localmente
* Python 3.x instalado

**Instalação das dependências:**
```
bash
pip install pymongo pandas
```
**Execução:**

```
bash
python script.py
```
**📊 Estrutura do Projeto**
```
text
movie-analysis/
├── data                   # Pasta para arquivos de dados
│   └── movies.csv              # Dataset de filmes
│   └──movies_5000.csv          # Dataset de filmes
│   └──movies_50000.csv         # Dataset de filmes
├── resultados
│   └── results.csv        # Resultados de cada consulta
├── docs
│   └── benchmark_plot.png  # Gráfico dos resultados
├── scripts
│   └── atualização.py      # Consulta de atualização
│   └── consulta_complexa.py    # Consulta Simples
│   └── consulta_simples.py     # Consulta Complexa
│   └── deleção.py              # Consulta de Deleção
│   └── grafico.py              # Script para gerar gráfico
│   └── insercao.py             # Inserção do dataset para as consultas
│   └── insercao_em_massa_50k.py    # Inserção de um data set com 50mil registros
│   └── insercao_em_massa_5k.py     # Inserção de um data set com 5mil registros
│
└── README.md              # Este arquivo
```
### 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

#### 📄 Trabalho realizado por fins de estudo
*Faculdade Unisales* -
*Mateus Cristo da Silva* - 
*Mikaella Cintra* - 
*Segunda parte do trabalho:* (https://github.com/MikaCintra/Benchmark-MySql)
