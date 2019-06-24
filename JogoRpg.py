def menu():
    print('-'*50)
    print('1 - Soco')
    print('2 - Chute')
    print('3 - Especial')
    print('-' * 50)


def ataqueheroi(op, expheroi):
    if op == 1:
        print("soco")
    elif op == 2:
        print("chute")
    elif op == 3:
        print("especial")


op = -1

#Inicio Jogo
while op != 0:
    menu()
    op = int(input('escolha'))





