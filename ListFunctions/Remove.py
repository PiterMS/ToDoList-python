# Essa daqui remove uma tarefa da lista
def remove (a = [], b = None):
        
        if b == None :
            try:
                b = int(input("Qual a tarefa a ser removida(Pegue pelo seu índice)\n"))
        
            except KeyboardInterrupt:
                print('Ocorreu um Erro, tente de novo')
            
            except ValueError:
                 print('Apenas números')

        for i in range(len(a)):
        
            if b - 1 == i:
                a.pop(i)
                print(f"A tarefa número {b} foi apagada")
                return
            elif b - 1 != i:
                print(f"{b} não existe")
                return

        else:
            a.pop(b-1)
