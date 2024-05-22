def primeiraMaiuscula(frase):
    frase = frase[0].upper() + frase[1:]
    return frase, len(frase)

if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    frase_maiuscula, tamanho = primeiraMaiuscula(frase)
    print("O tamanho da frase é: {}".format(tamanho))
    print(frase_maiuscula)