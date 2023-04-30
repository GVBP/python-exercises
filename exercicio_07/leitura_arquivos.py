with open('names.txt', 'r', encoding="utf-8") as open_file:
    nomes = open_file.read().splitlines()

contagem = {}

for nome in nomes:
    if nome in contagem:
        contagem[nome] += 1
    else:
        contagem[nome] = 1

for nome, count in contagem.items():
    print(f'{nome}: {count}')
