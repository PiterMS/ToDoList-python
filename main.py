import Funcoes

valor = 0
lista=[]
escolha = 0
j= True


while j ==True:
    Funcoes.pagina()

    escolha = int(input("Escolha uma das opçoes\n"))

    if escolha == 1:
        print("\n\n")
        Funcoes.show(lista)

    elif escolha == 2:
        valor = input("Qual a nova tarefa\n")
        Funcoes.create(lista,valor)

    elif escolha == 3:
        valor = int(input("Qual a tarefa a ser removida\n"))
        Funcoes.delete(lista, valor)

    elif escolha == 4:
        j = False
        print("Saindo...")

    else:
        print("\bError!! Reinicie!!!!\b")
        j = False