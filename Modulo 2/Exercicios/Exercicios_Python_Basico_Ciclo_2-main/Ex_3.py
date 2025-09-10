# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
numero_filmes=int(input('digite quantos filmes deseja? '))
conatador=0
while conatador<numero_filmes:
    filme=input('qual e o filme? ')
    filmes.append(filme)
    conatador=conatador+1
print(filmes)





# LOOP FOR
#numero_filmes=int(input('digite quantos filmes deseja? '))
#for i in range(numero_filmes):
#    filme=input('qual e o filme? ')
 #   filmes.append(filme)
#print(filmes)
    




