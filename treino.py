import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib

# Carregar o conjunto de dados Iris diretamente da biblioteca scikit-learn
from sklearn.datasets import load_iris

# Carregar o dataset Iris
iris = load_iris()
X = iris.data  # Features (variáveis preditoras)
y = iris.target  # Target (rótulo)

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Instanciar o modelo Naive Bayes
model = GaussianNB()

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy * 100:.2f}%")

# Salvar o modelo treinado em um arquivo .pkl
joblib.dump(model, 'naive_bayes_model.pkl')
