#from validators.video_id_validator import Validators
import re 


def verification_mat_operation(simbol):
    regex = re.compile(r"[-+\/*()%]")
    regex2 = re.compile(r"[**]")
    result = re.search(regex, simbol)
    result2 = re.search(regex2, simbol)
    if(result != None and len(simbol) == 1) or (result2 != None and len(simbol) == 2):
        return True
    else:
        return False
        
def verification_digit(number):
    regex = re.compile(r'\d')
    result = re.search(regex, number)
    if result != None:
        return True
    else:
        return False

