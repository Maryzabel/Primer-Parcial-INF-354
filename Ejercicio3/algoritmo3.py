import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

print("DATASET ORIGINAL")
print(datos)

from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer # otro algoritmo
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

#usando algoritmo 
#se usara este algoritmo para para rellenar los espacios vacios en el dataset
# una opcion es borrar las columnas con datos faltantes, pero eso afectaria al preprocesamiento de los datos
# para este caso se va a rrellenar utilizando la media
# ej: si en la COLUMNA de ranking hay datos faltantes se puede rellenar con la media, asi suponiendo que los usuarios sin datos, tiene  un ranking de la media del resto

imputer = SimpleImputer(strategy='mean')
ans = imputer.fit_transform(dataset_numerico)

datitos = pd.DataFrame(ans, columns = datos.columns)
print(datitos)
