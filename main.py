import os, time
def menunum():
    return("""
          1 | 2 | 3 | 4 | 5 |
          6 | 7 | 8 | 9 | 0 |
          + | - | / | * | = |
          """)
def menuope():
        return("""
          + | - | / | * | = |
          """)
def showresul(x):
    str(x)
    return(f"{x}")


n = 0

while True:
    print(showresul(n))
    print(menunum())
    n = input(" ")
    n = n
    os.system("cls")
    print(showresul(n))
    print(menuope())
    op = str(input(" ")) 
    resultado = f"{n} {op}"
    os.system("cls")
    print(showresul(resultado))
    print(menunum())
    n2 = input(" ")
    resueval = eval(resultado+str(n2))
    resultado = f"{n} {op} {n2} == {resueval}"
    os.system("cls")
    print(showresul(resultado))
    print(menuope())
    op = str(input(" "))
    while op != "=":
        os.system("cls")
        acu = resueval
        resultado = f"{acu} {op}"
        print(showresul(resultado))
        print(menunum())
        n2 = input(" ")
        os.system("cls")
        resueval = eval(resultado+str(n2))
        resultado = f"{acu} {op} {n2} == {resueval}"
        print(showresul(resultado))
        print(menuope())
        op = str(input(" "))
        time.sleep(3)
    os.system("cls")
    print(showresul(resultado))
    print("---------------------------------------------------------------------------")
    break
    
    