'''
Crie uma funcão em python que salve em um arquivo uma 
frase digitada pelo usuário
'''

def criaArquivo(texto):
    try:
        with open("arquivo.txt", "r+") as arquivo:
            conteudo = arquivo.readlines()
            conteudo.append(texto + "\n")
            arquivo.close()
        arquivo = open("arquivo.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()
    except Exception as e:
        print("Falha ao abrir aquivo: {}".format(e))

def lerArquivo():
    conteudo = open("arquivo.txt", "r")
    print(conteudo.read())
    conteudo.close

if __name__ == "__main__":
    texto = input("O que deseja gravar? ")
    criaArquivo(texto)


# with open("exemplo.txt", "r") as arquivo:
#     conteudo = arquivo.read()
# for item in conteudo:
#     print(item, end="")

# print(conteudo)
# arquivo = open("novo.txt", "w")
# arquivo.write("Alterando nosso primeiro arquivo\n")
# arquivo.write("Segunda linha\n")
# arquivo.close()
