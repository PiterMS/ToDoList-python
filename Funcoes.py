##Funções usada na arquivo principal


def create(a = [] ,b = None):
    if b == None: ##Verifica se "b" é Nulo
       b = input("Qual a nova tarefa")
       a.append(b)
    
    else:
        a.append(b)


def show(a): ##Printa as tarefas
    if not a:
        print("lista vazia")
        return
    
    for i in range(len(a)):        
        print (f"{i+1}. {a[i]}")
        
def delete(a = [], b = 0):#Remove as tarefas a partir do número dela segundo a função Show()
    for i in range(len(a)):
        
        if b - 1 == i:
            a.pop(i)
            print(f"A tarefa número {b} foi apagada")
            return
        elif b - 1 != i:
            print(f"{b} não existe")
            return
        

def pagina(): ##Só é uma função que serve para mostrar as opcões
    print("\n\n\n==== Lista de Tarefas ====\n")
    print("Opções:\n")

    print("\b 1. Mostrar lista\n")
    print("\b 2. Criar Tarefa\n")
    print("\b 3. Remover Tarefa\n")
    print("\b 4. Sair\n")
    return
        

