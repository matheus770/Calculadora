import re

def menunum():
    print("""
1 | 2 | 3 | 4 | 5 |
6 | 7 | 8 | 9 | 0 |
+ | - | / | * | = |
          """)
    
def menuope():
        print("""
+ | - | / | * | = |
          """)
        
def showresul(x):
    str(x)
    print(f"{x}")

def verification_mat_operation(simbol):
    # regex = re.compile(r"-|[+]|/|[*]|[**]|%")
    regex = re.compile(r"[-+\/*()=]")
    result = re.search(regex, simbol)
    if(result != None and len(simbol) == 1):
        return(True)
    else:
        return(False)
        
def verification_number(n):
    regex = re.compile(r"\d")
    result = re.search(regex, n)
    if result != None:
        return(True)
    else:
        return(False)

def inputnum():
    num = input("Número: ")
    if verification_number(num) == True:
        return num
    else:
        print("Erro, Isso não é um numero valido !!!")
     

def inputsimbol():
    simbol = input("Operação: ")
    if verification_mat_operation(simbol) == True:
        return simbol
    else:
        print("Erro, Isso não é um simbolo de operação matematica !!!")
       
    
