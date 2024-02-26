import pandas as pd

# Usando barras duplas no caminho do arquivo
arquivo = 'C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\PROJETOS VS\\Desafios\\pandas\\bd_h2.xlsx'
planilha = 'INTERESSADOS H2'

# Lendo o arquivo XLSX
df = pd.read_excel(arquivo, sheet_name=planilha)

print(df.head())


contagem = df['Área de atuação: '].value_counts()

mais_repetido = contagem.idxmax()

print(f"A area de atuação que mais se repetiu foi {mais_repetido}")
