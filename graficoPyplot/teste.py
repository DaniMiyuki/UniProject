import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = [1, 2, 3]
y = [4, 5, 6]
colors = ['red', 'blue', 'orange']

# Plotando o gráfico
pontos = plt.scatter(x, y, color=colors)

# Criando objetos Patch para cada cor
patches = [mpatches.Patch(color=color, label=f'Cor {color}') for color in colors]

# Adicionando a legenda ao gráfico
plt.legend(handles=patches)

plt.show()
