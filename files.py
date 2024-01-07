import os

# Pasta atual onde os arquivos serão criados
caminho_pasta = os.getcwd()

# Loop para criar arquivos de ex036.py até ex045.py
for i in range(57, 101):
    nome_arquivo = f'ex{i:03d}.py'
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    
    # Criação de arquivos vazios
    with open(caminho_arquivo, 'w'):
        pass
    print(f'Arquivo {nome_arquivo} criado com sucesso na pasta atual.')
