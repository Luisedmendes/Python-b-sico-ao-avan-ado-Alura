import random

def jogar():

    print(20*"-_")
    print("**Bem vido ao jogo da adivinhação**")
    print(20*"-_")

    numero_secreto = random.randint(1,100)
    numero_rodadas = 1
    pontos = 1000

    print("Qual nível você quer jogar? 1-fácil 2-normal 3-dificil")
    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        numero_tentativas = 10
    elif (nivel == 2):
        numero_tentativas = 5
    else:
        numero_tentativas = 3

    for numero_rodadas in range(1, numero_tentativas+1):
        print(f'você tem {numero_rodadas} de {numero_tentativas} tentativas ainda')

        chute = int(input("Digite seu número: "))
        print("Você digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Você digitou um número inválido")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou!\nFez {pontos}")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            numero_rodadas += 1
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()

