import numpy as np
import matplotlib.pyplot as plt

# 1. Conjunto de dados (Exemplo: Idades)
lista_idades = [26, 30, 32, 22, 26, 35, 400, 20, 43, 31, 23]

# 2. Cálculos Estatísticos
media = np.mean(lista_idades)
desvio = np.std(lista_idades)

# 3. Identificação de Outliers (Regra dos 3 desvios padrões)
limite_superior = media + 3 * desvio
limite_inferior = media - 3 * desvio

print(f"Média: {media:.2f}")
print(f"Limite Superior: {limite_superior:.2f}")
print(f"Limite Inferior: {limite_inferior:.2f}")

# 4. Visualização com Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(lista_idades)
plt.title("Identificação de Outliers nas Idades")
plt.show()