import pandas as pd
import numpy as np
import statistics as stat

url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']


################################# FUNCIONES ################################################
def promedio():
  print("CALCULANDO EL PROMEDIO POR COLUMNAS")
  for i in range(len(dataset[0])):
    if( type(dataset[0][i]) != str): 
      print(titles[i], np.mean(datos[titles[i]]))
  print()

def moda():
  print("\nCALCULANDO LA MODA POR COLUMNAS")
  for i in range(len(dataset[0])):
    print(titles[i], stat.mode(datos[titles[i]]))
  print()

def quartil(k):
  print("quartil Numpy", k)
  datos1 = pd.DataFrame(datos)
  datos2 = datos1.select_dtypes(include=[np.number])
  print(np.percentile(datos2, k, axis = 0))
  print()

def quartilPanda(k):
  print("quartil Panda", k)
  df = pd.DataFrame(datos)
  text_cols = []
  for col in df.columns:
      if df[col].dtype == object:
          text_cols.append(col)

  df = df.drop(text_cols, axis=1)
  q1 = df.quantile(k)
  print(q1)
  print()

def PercentilePanda(k):
  print("Percentile Panda", k)
  df = pd.DataFrame(datos)
  text_cols = []
  for col in df.columns:
      if df[col].dtype == object:
          text_cols.append(col)

  df = df.drop(text_cols, axis=1)
  q1 = df.quantile(k)
  print(q1)
  print()
 

##################################### PRINCIPAL ############################################
print("CALCULANDO CON NUMPY")
promedio()
moda()
quartil(25)
quartil(50)
quartil(75)
#la funcion percentil de numpy halla tanto quartil como percentil
quartil(80)


quartilPanda(0.25)
quartilPanda(0.5)
quartilPanda(0.75)

#la funcion quantile de numpy halla tanto quartil como percentil
PercentilePanda(0.8)



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

