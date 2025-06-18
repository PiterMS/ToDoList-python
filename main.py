# Eu poderia usar o "*" para chamar todo mundo, mas essa bomba fiacava dando erro entao fiz desse jeito
from ListFunctions import showlist as S
from ListFunctions import createtask as C
from ListFunctions import Remove as R


loop = True
lista = []
escolha = 0
valor = None



while loop == True:
    
    # Melhor coisa q fiz a para pagina inicial    
    t = open('title.txt', 'r')
    print(t.read())


    print('\n'*2,
        ' 1. Mostrar Lista   2. Criar Tarefa  3. Remover Tarefa  4. Sair', '\n'*3)

    # Execeçoes para impedir q o eu bata a cabeça no teclado é quebre o programa
    try:
        escolha = int(input("Escolha sua opção\n"))
    except KeyboardInterrupt:
        print("Erro refaça!!\n\n")

    except ValueError:
        print('Use apenas números\n\n')

    


    if escolha == 1:
        S.showlist(lista)
    
    elif escolha == 2:
        C.createtask(lista, valor)

    elif escolha == 3:
        
        S.showlist(lista)
        R.remove(lista,valor)
    
    elif escolha >= 4 : 
        loop = False
        print("\n\n Finalizando...\n\n")