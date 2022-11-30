import random


def jogar():

    welcome_msg_()

    palavra_secreta = load_secret_word()

    letras_acertadas = str(len(palavra_secreta) * "_")
    letras_acertadas_list = list(letras_acertadas)

    enforcou = False
    acertou = False

    tentativas = int(len(palavra_secreta) + 2)
    erros = 0

    print(letras_acertadas_list)

    while not enforcou and not acertou:

        chute = str(input("Qual letra? ").strip().upper())

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas_list[index] = letra
                index = index + 1

        else:
            erros += 1
            print("Errou {} de {}.".format(erros, tentativas))

        if "_" not in letras_acertadas_list:
            acertou = True
            print(
                "\nVocê venceu!! Porcentagem de acerto foi: {:.2%}\n".format(
                    1 - (erros / tentativas)
                )
            )

        enforcou = erros == tentativas
        print(letras_acertadas_list)

    print("Fim do jogo")


def welcome_msg_():
    print("*********************************")
    print("*****Welcome to Hangman Game*****")
    print("*********************************")


def load_secret_word():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.replace("\n", "")
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if __name__ == "__main__":
    jogar()
