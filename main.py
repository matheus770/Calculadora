n = 0
while True:
    n = float(input("Numero: "))
    print("Digite o simbolo da operação: ")
    op = str(input(f"{n} "))
    n2 = float(input(f"{n} {op} "))
    sm = f"{n}{op}{n2}"
    sm = eval(sm)
    print(sm)
    dj = int(input("1 == continuar \n2 == Outra conta \n3 == Sair\n"))
    if(dj == 1 ):
        while True:
            print("Digite o simbolo da operação: ")
            op = str(input(f"{sm} "))
            n2 = float(input(f"{sm} {op} "))
            sm = f"{sm}{op}{n2}"
            sm = eval(sm)
            print(sm)
            dj = int(input("1 == continuar \n2 == Sair\n"))
            if(dj == 1):
                continue
            else:
                break
    elif(dj == 2):
        continue
    elif(dj == 3):
        break
    