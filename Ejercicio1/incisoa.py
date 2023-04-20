import pandas as pd
import numpy as np
import statistics as stat

url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']




#################################################3
# RESULTADO EN FUNCIONES

def promedio():
  print("CALCULANDO EL PROMEDIO POR COLUMNAS")
  for i in range(len(dataset[0])):
    sum = 0;
    if( type(dataset[0][i]) != str):
      for j in range(len(dataset)):
        sum += dataset[j][i];
      sum /= len(dataset)
    
    print(titles[i], sum)
  print()

def moda():
  print("CALCULANDO LA MODA POR COLUMNAS")
  for i in range(len(dataset[0])):
    mapa = {}
    for j in range(len(dataset)):
      if(dataset[j][i] in mapa):
        mapa[dataset[j][i]] += 1;
      else:
        mapa[dataset[j][i]] = 1;
    
    lista = []
    for key, value in mapa.items():
      lista.append([value, key])
    # print(titles[i], "mapita " , len(mapa))
    lista.sort(reverse=True)
    print(titles[i], lista[0][1])
  print()

def cuartil(k):
  print("QUARTIL ", k)
  for i in range(len(dataset[0])):
    sum = 0;
    if( type(dataset[0][i]) != str):
      vector = []
      for j in range(len(dataset)):
        vector.append(dataset[j][i])

      vector.sort()
      cur = k * (len(vector) + 1) / 4
      pos = int(cur)
      print(titles[i], end=  ' ')

      if(cur == pos):
        # quartil es exacto
        print(vector[pos - 1])
      else:
        x1 = vector[pos - 1]
        x2 = vector[pos]
        total = abs(x2 + x1) / 2
        print(total)
  print()



def percentil(k):
  print("PERCENTIL ", k)
  for i in range(len(dataset[0])):
    sum = 0;
    if( type(dataset[0][i]) != str):
      vector = []
      for j in range(len(dataset)):
        vector.append(dataset[j][i])

      vector.sort()
      cur = k * (len(vector) + 1) / 100
      pos = int(cur)
      print(titles[i], end=  ' ')

      if(cur == pos):
        # quartil es exacto
        print(vector[pos - 1])
      else:
        x1 = vector[pos - 1]
        x2 = vector[pos]
        total = abs(x2 + x1) / 2
        print(total)
  print()



####################################################333



############################### MENU PRINCIPAL #####################################################
promedio()
moda()
cuartil(1);
cuartil(2);
cuartil(3);

percentil(80);




"""
suponiendo la columna de "ranking", aplica para el resto
el promedio es 2022.4267933180479 eso quiere decir que de todos los usuarios registrados
tenemos ese rendimiento promedio en cada concurso

para la moda es 1978 , quiere decir que de todo el ranking ese valor es el mas comun
muchos usuarios estan con ese ranking

para el quartil 2 (50%) para el ranking es igual a 2023
eso quiere decir que la mitad de los usuairos tiene un ranking de 2023, es decir estan en un rendimiento promedio

para los percentiles (80)
se tiene 2111
eso nos quiere decir que el 80 % de los usuarios tiene ese ranking, lo que significa que muchos usuarios tienen rendimiento
promedio, no son muy pros (considerando a los pros de ranking 3000 para arriba)
"""


