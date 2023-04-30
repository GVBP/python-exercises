def create_list(lista):
    nova_lista = []
    for elemento in lista.split(","):
        nova_lista.append(elemento.strip())
    return nova_lista

def remove_duplicatas(lista):
    return list(set(lista))

lista_original = input("Digite uma lista de números separados por vírgula: ")
lista_original = create_list(lista_original)
nova_lista = remove_duplicatas(lista_original)
print(nova_lista)
