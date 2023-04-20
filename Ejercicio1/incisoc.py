import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

#columnas a graficar

x = datos['Username']
y = datos['Rating']
# x = datos['Rating']
# y = datos['Country']
plt.bar(x,y)

plt.title("Rating") #a la final mundial icpc
plt.xlabel("Usuarios")
plt.ylabel("Ranking")

plt.show()

"""
El significado del grafico es el siguiente

en el eje  X tenemos a cada usuario
en el eje Y tenemos el el ranking 

entonces se muestra el ranking por usuario, se puede ver,que la mayoria de los usuarios estan por debajo del ranking 2700, 
y muy pocos arriba, de hecho casi el 80% estan por debajo, lo que claramente nos dice que hay muy pocos usuarios que son realmente muy buennso
en programación competitiva, lo cual no quiere decir que los demas sean malos
"""

