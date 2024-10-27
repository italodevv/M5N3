# Importando a biblioteca pandas
import pandas as pd

# Microatividade 1: Ler um arquivo CSV
arquivo_csv = 'database.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', header=None)  # Usando ponto e vírgula como delimitador e sem cabeçalho

# Exibindo os dados lidos
print("Dados lidos do arquivo CSV:")
print(dados)

# Renomeando as colunas para facilitar a manipulação
dados.columns = ['Coluna1', 'Coluna2', 'Data', 'Coluna4', 'Coluna5', 'Coluna6']

# Microatividade 2: Criar um subconjunto de dados
subconjunto_dados = dados[['Coluna1', 'Coluna2', 'Data']]
print("\nSubconjunto de dados:")
print(subconjunto_dados)

# Microatividade 3: Configurar o número máximo de linhas a serem exibidas
pd.set_option('display.max_rows', 9999)

# Exibindo o conjunto de dados original com a configuração atual
print("\nConjunto de dados original com todas as linhas:")
print(dados.to_string())

# Microatividade 4: Exibir as primeiras e últimas 10 linhas
print("\nPrimeiras 10 linhas do conjunto de dados:")
print(dados.head(10))

print("\nÚltimas 10 linhas do conjunto de dados:")
print(dados.tail(10))

# Microatividade 5: Exibir informações gerais sobre o conjunto de dados
print("\nInformações gerais sobre o conjunto de dados:")
info = dados.info()
print(info)

# Obtendo informações específicas
total_linhas = dados.shape[0]
total_colunas = dados.shape[1]
dados_nulos = dados.isnull().sum().sum()
tipos_dados = dados.dtypes
memoria_usada = dados.memory_usage(deep=True).sum()

print(f"\nTotal de linhas: {total_linhas}")
print(f"Total de colunas: {total_colunas}")
print(f"Quantidade de dados nulos: {dados_nulos}")
print(f"Tipo de dado de cada coluna:\n{tipos_dados}")
print(f"Quantidade de memória utilizada: {memoria_usada} bytes")
