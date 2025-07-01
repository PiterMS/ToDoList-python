## Essa função serve para adicionar uma nova tarefa a lista
def createtask (a = [], b = None):
    if b == None :
        try:
            b = input("Qual a nova tarefa\n")
            a.append(b)

        except KeyboardInterrupt:
            print('Ocorreu um Erro, tente de novo')

    else:
        a.append(b)
