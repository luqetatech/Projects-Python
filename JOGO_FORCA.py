import random

def escolher_palavra():
    palavras = {
        "python": "Linguagem de programação",
        "javascript": "Linguagem de script do lado do cliente",
        "frontend": "Parte de um site que interage com o usuário",
        "backend": "Parte de um site que lida com o servidor",
        "java": "Linguagem de programação orientada a objetos"
    }
    palavra, dica = random.choice(list(palavras.items()))
    return palavra, dica

def jogar_forca():
    palavra, dica = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 5
    ponto = 100

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")
    print(f"Dica: {dica}")

    while True:
        palavra_secreta = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_secreta += letra
            else:
                palavra_secreta += "_"

        print(palavra_secreta)
        print("")

        if palavra_secreta == palavra:
            print(f"Parabéns! Você acertou a palavra ({palavra}) com {ponto} pontos.")
            break

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            if tentativa not in letras_corretas:
                print("Letra correta!")
                letras_corretas.append(tentativa)
            else:
                print("Você já adivinhou essa letra. Tente outra.")
        else:
            if tentativa not in letras_erradas:
                print("Letra errada! Tente novamente.")
                letras_erradas.append(tentativa)
                tentativas -= 1
                ponto -= 10
                print(f"Você tem {tentativas} tentativas restantes.")
            else:
                print("Você já tentou essa letra errada. Tente outra.")

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

if __name__ == "__main__":
    jogar_forca()
