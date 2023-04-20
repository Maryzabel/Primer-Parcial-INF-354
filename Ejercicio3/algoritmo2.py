import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

print("DATASET ORIGINAL")
print(datos)

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler # otro algoritmo
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

#EXPLICACION DEL ALGORITMO
#se usara este algoritmo para que todas las caracteristicas del data set, tengan la misma escala, esto es para  mejorar la presicion del modelo
# en realcion al entrenamiento

scaler = StandardScaler()
ans = scaler.fit_transform(dataset_numerico)

datitos = pd.DataFrame(ans, columns = datos.columns)
print(datitos)
