import matplotlib.pyplot as plt

operations = ['Inserção', ' Simples', ' Complexa', 'Atualização', 'Deleção']
times = [0.2305, 0.0121, 0.1707, 0, 0]  # Substitua pelos tempos reais
plt.bar(operations, times)
plt.xlabel('x Operação')
plt.ylabel('y Tempo (segundos)')
plt.title('Desempenho MongoDB - Benchmark')
plt.savefig('docs/benchmark_plot.png')
plt.show()