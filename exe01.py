#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
print("miguel do amaral paes ronda")
paises= ('brasil,colombia,italia,marrocos,inglaterra')
print(paises)
selecao_paises = (input("digite um país"))
if selecao_paises in paises:
    indice = paises.index(selecao_paises)
    print(" o indice do pais e ", indice)
else:
    print("PAIS ESTE PAIS NAO ESTA REGISTRADO")