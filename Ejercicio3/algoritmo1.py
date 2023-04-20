import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

print("DATASET ORIGINAL")
print(datos)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
dataset_numerico = []
for i in range(len(dataset[0])):
  aux = []
  for j in range(len(dataset)):
    aux.append(dataset[j][i])
  aux_2 = encoder.fit_transform(aux);
  dataset_numerico.append(aux_2)


print("NUEVO DATA SET APLICADO ALGORITMO")
dataset_numerico = np.array(dataset_numerico)
dataset_numerico = dataset_numerico.transpose() # transponiendo para que este en columnas (como estaba originalmanete)
"""
EXPLICACIÓN
Este algoritmo se esta usango porque justo en el dataset se tiene columnas que son de tipo string,
y al hacer operaciones sobre esas columnas se  necesita que sean de tipo number, y LabelEncoder()
codificar las cadenas -> es como si a cada cadenas de la un hash (un numero) y reemplaza todas las cadenas con ese mismo nuevo numero
para el dataset en la columna "Country" nos sirve de mucho ya que  podemos poener a entrenarlo utilizando dicha columna
"""

datitos = pd.DataFrame(dataset_numerico, columns = datos.columns)
print(datitos)
