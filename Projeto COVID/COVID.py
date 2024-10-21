import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm

# 1. Coleta de Dados
# Supondo que temos um arquivo CSV com dados de COVID-19
# Exemplo: "dados_covid_brasil.csv"
url = "https://example.com/dados_covid_brasil.csv"  # Substitua pelo link real
dados = pd.read_csv(url)

# Exibir as primeiras linhas do dataframe
print(dados.head())

# 2. Análise Exploratória
# Converter a coluna de data para o formato de data
dados['data'] = pd.to_datetime(dados['data'])

# Gráfico de casos confirmados ao longo do tempo
plt.figure(figsize=(14, 7))
sns.lineplot(data=dados, x='data', y='casos_confirmados', label='Casos Confirmados')
sns.lineplot(data=dados, x='data', y='obitos', label='Óbitos', color='red')
plt.title('Casos Confirmados e Óbitos ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Casos')
plt.legend()
plt.show()

# 3. Modelagem Preditiva
# Preparar dados para modelagem
dados['dias'] = (dados['data'] - dados['data'].min()).dt.days
X = dados[['dias']]
y = dados['casos_confirmados']

# Dividir em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Previsão
y_pred = modelo.predict(X_test)

# Avaliação do modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Gráfico de Previsão
plt.figure(figsize=(14, 7))
plt.scatter(X_test, y_test, color='blue', label='Dados Reais')
plt.scatter(X_test, y_pred, color='orange', label='Previsões')
plt.title('Previsão de Casos Confirmados')
plt.xlabel('Dias desde o Início da Pandemia')
plt.ylabel('Número de Casos Confirmados')
plt.legend()
plt.show()

# 4. Modelagem de Séries Temporais (ARIMA)
model = sm.tsa.ARIMA(dados['casos_confirmados'], order=(5, 1, 0))
model_fit = model.fit()
print(model_fit.summary())

# Previsão de 30 dias
forecast = model_fit.forecast(steps=30)
plt.figure(figsize=(14, 7))
plt.plot(dados['data'], dados['casos_confirmados'], label='Casos Confirmados', color='blue')
plt.plot(pd.date_range(start=dados['data'].max(), periods=30, freq='D'), forecast, label='Previsão', color='orange')
plt.title('Previsão de Casos Confirmados para os Próximos 30 Dias')
plt.xlabel('Data')
plt.ylabel('Número de Casos Confirmados')
plt.legend()
plt.show()

