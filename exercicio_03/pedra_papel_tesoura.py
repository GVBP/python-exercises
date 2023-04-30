jogando = True
while jogando:
    while True:
        jogada1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
        if jogada1 == "pedra" or jogada1 == "papel" or jogada1 == "tesoura":
            break
        print("Jogador 1, escolha inválida!");
    while True:
        jogada2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()
        if jogada2 == "pedra" or jogada2 == "papel" or jogada2 == "tesoura":
            break
        print("Jogador 2, escolha inválida!");

    if jogada1 == jogada2:
        print("Empate!")
    elif (jogada1 == "pedra" and jogada2 == "tesoura") or (jogada1 == "papel" and jogada2 == "pedra") or (jogada1 == "tesoura" and jogada2 == "papel"):
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

    jogar_novamente = input("Desejam jogar novamente? (sim ou nao): ").lower()
    if jogar_novamente != "sim":
        jogando = False
