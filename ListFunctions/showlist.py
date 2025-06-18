def showlist(a = []):
    if not a:
        print("\nLista vazia\n\n")
        return
    
    print('\n'*2)
    for i in range (len(a)):
        print(f"{i+1}. {a[i]}")

    