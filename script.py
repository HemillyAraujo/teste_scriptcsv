import csv

# 1. abrir o arquivo
with open('0_dados_history.csv', encoding='utf-8') as arquivo_referencia:
    tabela = csv.reader(arquivo_referencia, delimiter=',') # 2. ler a tabela
    for l in tabela: # 3. navegar pela tabela
        id_autor = l[0]
        nome = l[1]
        print(id_autor, nome) # 191149, Diego C B Mariano
