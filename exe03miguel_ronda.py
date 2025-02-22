#- Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. 
# Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não".
#  Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes, 
# exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. 
# Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
print("miguel do amaral paes ronda")
produto = ()
adici_prod = list(produto)
for i in range(10):
    produto = input("insira o nome do produto; ")
    adici_prod.append(produto)
    produto = tuple(adici_prod)

print(produto)
nom = input("insira um nome de um produto; ")

if nom in produto:
    for i in range(len(produto)):
        if produto[i] == nom:
            print(i)

else:
    print("esse produto nao foi inserido")

numero = int(input("insira um numero entre 0 e 9 "))
print(produto[numero])

