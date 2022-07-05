from verifications import verification_digit, verification_mat_operation
import os

n = 0
while True:
    n = input("Numero: ")
    if verification_digit(n) == True:
        print("Digite o simbolo da operação: ")
        op = str(input(f"{n} "))
        if verification_mat_operation(op) == True:
            n2 = input(f"{n} {op} ")
            if verification_digit(n2) == True:
                sm = f"{n}{op}{n2}"
                sm = eval(sm)
                print(sm)
                dj = int(input("1 == continuar conta \n2 == Outra conta \n3 == Sair\n"))
                if verification_digit(dj) == True:
                    if(dj == 1 ):
                        while True:
                            print("Digite o simbolo da operação: ")
                            op = str(input(f"{sm} "))
                            if verification_mat_operation(op) == True:
                                n2 = float(input(f"{sm} {op} "))
                                if verification_digit(n2) == True:
                                    sm = f"{sm}{op}{n2}"
                                    sm = eval(sm)
                                    print(sm)
                                    dj = int(input("1 == continuar \n2 == Sair\n"))
                                    if verification_digit(dj) == True:
                                        if(dj == 1):
                                            continue
                                        elif(dj == 2):
                                            continue
                                        elif(dj == 3):
                                            break
                                    else:
                                        print("Escolha uma opção numerica !")
                                        os.system("cls")
                                else:
                                    print("Digite um numero !")
                                    os.system("cls")
                            else:
                                print("Digite um simbolo de operação matematica na proxima !")
                                os.system("cls")
                    elif(dj == 2):
                        continue
                    elif(dj == 3):
                        break
                else:
                    print("Escolha uma opção numerica !")
                    os.system("cls")
            else:
                print("Digite um numero !")
                os.system("cls")
        else:
            print("Digite um simbolo de operação matematica na proxima !")
            os.system("cls")
    else:
        print("Digite um numero !")
        os.system("cls")

    