import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

# Lectura de Datos
setInicial = pd.read_csv('') # path .csv etiquetados

atributosName = setInicial.columns[:-1].values
atributoClase = setInicial.columns[-1]

dataGral = setInicial[atributosName]
claseGral = setInicial[atributoClase]

# Separación de Conjuntos (70% - 30%)
X = setInicial.drop(columns=['plagio']) # cambiar a nombre de columna final
y = setInicial['plagio'] # cambiar a nombre de columna final

valoresTrain, valoresTest, clasesTrain, clasesTest= \
    train_test_split(X, y, test_size=0.30, stratify=y)

# Transformación de Datos
scaler = StandardScaler()

valoresTrain_T = scaler.fit_transform(valoresTrain)
valoresTest_T = scaler.transform(valoresTest)

# Implementación Naive Bayes
model = GaussianNB()
model.fit(valoresTrain_T, clasesTrain)

proba_train = model.predict_proba(valoresTrain_T)
proba_test = model.predict_proba(valoresTest_T)

# ....SIGUE....
