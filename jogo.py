import forca
import numero_secreto

def escolhe_jogo():
    print(20*"-_")
    print("**Escolha o seu jogo**")
    print(20*"-_")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        numero_secreto.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
