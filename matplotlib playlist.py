import matplotlib.pyplot as plt

plt.style.use('dark_background')

idade = [14, 15, 16, 18, 22, 25, 28, 29, 30, 31, 33, 35, 38, 40, 45, 55, 50]
salario = [1100, 1350, 1350, 1400, 2100, 2500, 2580, 3000, 3000, 3300, 3580, 10000, 
           14258, 15500, 15500, 16000, 16500]
plt.plot(idade, salario, marker = '*', 
         color = 'red', linestyle = '--', label = "IT Professionals")

salario_python = [3300, 3300, 5000, 5200, 5250, 5380, 5800, 5890, 5900,
                  5995, 6100, 6200, 6250, 12000, 15000, 15300, 20000]
plt.plot(idade, salario_python, marker = 'o', 
         color = 'blue', linestyle = '-.', label = "Python Dev")

plt.ylabel('Salário ')
plt.xlabel('Idade')
plt.tight_layout()

plt.legend()
plt.title("Treinando gráficos em Python")
plt.show()