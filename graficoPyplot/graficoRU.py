import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np



class FuncaoLinear:
    def __init__(self, cfl1, cfl2, cfl3): 
        self.cfl1 = cfl1
        self.cfl2 = cfl2
        self.cfl3 = cfl3


    def calcular_funcao(self, x):
        return self.cfl1 * x + self.cfl2 * x - self.cfl3
    
    @staticmethod
    def vetor(n):
        lista = []
        for i in range (n):
            n = int(input("Digite 10 numeros de [0 a 99]: "))
            lista.append(n)
        return lista
def legenda(cores, x, y):
    for i in cores:
        return i   

# Instancia da classe FuncaoLinear
funcao = FuncaoLinear(4, 5, 5)


# Definicao dos valores de x
lista = FuncaoLinear.vetor(10)

x = np.array(lista)
y = np.array([funcao.calcular_funcao(valor_x) for valor_x in x])

# Tracando o grafico de dispersao com cores
cores = ['red', 'green', 'blue', 'pink', 'orange', 'purple', 'black', 'grey', 'yellow', 'cyan']
plt.scatter(x,y, color = cores)
# Criando objetos Patch para cada cor
patches = [mpatches.Patch(color=color, label=f'x={x[i]}, y={y[i]}') for i, color in enumerate(cores)]

# Adicionando a legenda ao gráfico
plt.legend(handles=patches)

plt.xlabel('Eixo X', color="hotpink")
plt.ylabel('Eixo Y', color="hotpink")
plt.title('Grafico da funcao linear: y = ax + bx -c', color = "hotpink")
plt.grid(True)
plt.show()