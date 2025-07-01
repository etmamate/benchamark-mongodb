import matplotlib.pyplot as plt

operations = ['Inserção', ' Simples', ' Complexa', 'Atualização', 'Deleção']
times = [0.2291, 0.0110, 0.0231, 0.1172, 0.0225]  # Substitua pelos tempos reais
plt.barh(operations, times)
plt.xlabel('x Tempo (segundos)')
plt.ylabel('y Operação')
plt.title('Desempenho MongoDB - Benchmark')
plt.savefig('docs/benchmark_plot.png')
plt.show()