import random

jogando = True
while jogando:
    numero = random.randint(1, 9)
    tentativa = int(input("Adivinhe o número entre 1 e 9 (ou digite 0 para sair): "))
    if tentativa == 0:
        break
    if tentativa == numero:
        print("Parabéns, você acertou!")
    elif tentativa < numero:
        print("Sua tentativa foi menor do que o número correto.")
    else:
        print("Sua tentativa foi maior do que o número correto.")

print("O jogo acabou. Obrigado por jogar!")
