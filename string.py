'''
upper(): converte a string para maiúsculas.
lower(): converte a string para minúsculas.
strip(): remove espaços em branco do início e do final da string.
replace( antiga, nova ): substitui todas as ocorrências de antiga 
                         por nova na string.
split( separador ): divide a string em uma lista de substrings, 
                    utilizando o separador como delimitador.
find( substring ): retorna o índice da primeira ocorrência de 
                   substring na string (ou -1 se não encontrada).
'''

saudacao = "Bom dia"
nome = "Jefferson"

frase = "Tudo me é permitido, mas nem tudo me convém!"

print(frase.find("m"))

# frase = frase.replace("mas", "porém")
# print(len(frase))

print(frase[0:len(frase)])


# print(saudacao + ", " + nome)

# print(nome.upper()) # Escreve tudo em maiusculo
# print(nome.lower()) # Escreve tudo em minusculo


 # type: ignore