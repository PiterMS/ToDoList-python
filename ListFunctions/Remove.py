# Essa daqui remove uma tarefa da lista
def deletetask (a = [], b = None):
        
        if b == None :
            try:
                b = int(input("Qual a tarefa a ser removida(Pegue pelo seu índice)\n"))
        
            except KeyboardInterrupt:
                print('Ocorreu um Erro, tente de novo')
            
            except ValueError:
                 print('Apenas números')

        a.pop(b-1)
