from funciones import *

while(TRUE):
    menu()
    o = input("===> ")
    try:
        if(int(o) ==1):
            addDebitos()
        if(int(o) == 2):
            addcreditos()
        if(int(o) == 3):
            totalDebitosf()
        if(int(o) == 4):
            totalCreditosf()
        if(int(o) == 5):
            saldo()
        if(int(o) == 6):
            promedioDebitos()
        if(int(o) == 7):
            debitoGrande()
        if(int(o) == 8):
            registro()
        if(int(o) == 9):
            prnt()
        if(int(o) ==10):
            eliminar()
  
        if(int(o) <=0 | int(o) > 10):
            break
    except ValueError:  
        break