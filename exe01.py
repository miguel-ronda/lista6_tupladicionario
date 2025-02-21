#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
print("miguel do amaral paes ronda")

tupla_paises = ("Brasil", "Argentina", "Alemanha", "Japão", "França")


print("Tupla de países:", tupla_paises)

pais_selecao = input("Digite o nome de um país da lista acima: ")


if pais_selecao in tupla_paises:
    i = tupla_paises.index(pais_selecao)
    print("O índice do país {}} é: {}".index(tupla_paises,i))
else:
    print("O país inserido não está na lista.")