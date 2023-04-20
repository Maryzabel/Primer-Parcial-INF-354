import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

#seleccionando 4 columnas y 20 filas al azar
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
filas_ale = datos.sample(axis = 1, n = 4)
# print(filas_ale)
datos_final = filas_ale.sample(n = 20)
# print("DATOS ALEATORIOS\n", datos_final)


# puede que tengamos filas en cadenas debemos mapearlos a enteros
# para esto se uitlizara el preprocesamiento labelEncoder
dataset_aleatorio = datos_final.to_numpy()
# print("generando dataset aleatorio con numpy")
# print(dataset_aleatorio)
encoder = LabelEncoder()
dataset_numerico = []
for i in range(len(dataset_aleatorio[0])):
  aux = []
  for j in range(len(dataset_aleatorio)):
    aux.append(dataset_aleatorio[j][i])
  # dataset_numerico.append(aux)
  # print(aux)
  aux_2 = encoder.fit_transform(aux);
  # print(aux_2)
  dataset_numerico.append(aux_2)



print("NUEVO DATA SET")
dataset_numerico = np.array(dataset_numerico)
dataset_numerico = dataset_numerico.transpose() # transponiendo para que este en columnas (como estaba originalmanete)
print(dataset_numerico)


matriz = pd.DataFrame(dataset_numerico, columns = datos_final.columns)
print(matriz)
valor = matriz.columns[0] # como es aleatorio hallando cualquier columna
print("valor\n", valor)

X = matriz.drop(valor, axis = 1)
y = datos_final[valor]

print("variables\n")
print(X)
print("exis")
print(y)


resultado = DecisionTreeClassifier(max_depth=4, criterion='entropy', splitter= 'best')
resultado.fit(X = X, y = y)
DecisionTreeClassifier()
print(resultado.classes_)
print(resultado.criterion)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)
print(X_test)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 20))
plot_tree(decision_tree = resultado, feature_names = X.columns, filled = True, fontsize=12); #este punto y coma para que no muestre el texto que suele salir




