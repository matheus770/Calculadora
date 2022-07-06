import os, time
from funcs import *

n = 0

while True:
    showresul(n)
    menunum()
    n = inputnum()
    os.system("cls")
    showresul(n)
    menuope()
    op = inputsimbol()
    resultado = f"{n} {op}"
    os.system("cls")
    showresul(resultado)
    menunum()
    n2 = inputnum()
    resueval = eval(resultado+str(n2))
    resultado = f"{n} {op} {n2} == {resueval}"
    os.system("cls")
    showresul(resultado)
    menuope()
    op = inputsimbol()
    while op != "=":
        os.system("cls")
        acu = resueval
        resultado = f"{acu} {op}"
        showresul(resultado)
        menunum()
        n2 = inputnum()
        os.system("cls")
        resueval = eval(resultado+str(n2))
        resultado = f"{acu} {op} {n2} == {resueval}"
        showresul(resultado)
        menuope()
        op = inputsimbol()
        time.sleep(3)
    os.system("cls")
    showresul(resultado)
    print("---------------------------------------------------------------------------")
    break
    
    