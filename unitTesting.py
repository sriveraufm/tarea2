import unittest
# from funciones import *
from pickle import TRUE
debitos = []
registroDebito = 0
creditos = []
registrocreditos = 0
totalDebitos = 0
totalCreditos = 0
registroEliminar = 0

def totalDebitosf(debitosArray):
    global totalDebitos
    totalDebitos = 0
    for i in range(0,len(debitosArray)):
        totalDebitos += debitosArray[i]
    print("El total de debitos es: ",totalDebitos)
    return(totalDebitos)

def totalCreditosf(creditosArray):
    global creditos
    global totalCreditos
    totalCreditos = 0
    for i in range(0,len(creditosArray)):
        totalCreditos += creditosArray[i]
    print("El total de creditos es: ",totalCreditos)
    return(totalCreditos)

def promedioDebitos(debitosArray):
    promedio = 0
    if(totalDebitosf(debitosArray) > 0):
        promedio = totalDebitosf(debitosArray)/len(debitosArray)
    print("El promedio de debitos es: ",promedio)
    return(promedio)

def saldo(debitosArray,creditosArray):
    saldo = totalCreditosf(creditosArray) - totalDebitosf(debitosArray)
    print("El saldo actual es: ", saldo)
    return(saldo)

def debitoGrande(debitosArray):
    gg = 0
    for i in range(0,len(debitosArray)):
        if(debitosArray[i]>gg):
            gg = debitosArray[i]
    print("El debito mas grande es: ",gg)
    return(gg)

class TestCuboid(unittest.TestCase):
    
    def test_array1(self):
        debitosArray = [1,1,1,1,1,1,1,1,1,1]
        creditosArray = [1,1,1,1,1]
        self.assertAlmostEqual(totalDebitosf(debitosArray),10)
        self.assertAlmostEqual(totalCreditosf(creditosArray),5)
        self.assertAlmostEqual(promedioDebitos(debitosArray),1)
        self.assertAlmostEqual(saldo(debitosArray,creditosArray),-5)
        self.assertAlmostEqual(debitoGrande(debitosArray),1)
    
    def test_array2(self):
        debitosArray = [0,0,0,0,0,0,0,0,0,0]
        creditosArray = [0,0,0,0,0]
        self.assertAlmostEqual(totalDebitosf(debitosArray),0)
        self.assertAlmostEqual(totalCreditosf(creditosArray),0)
        self.assertAlmostEqual(promedioDebitos(debitosArray),0)
        self.assertAlmostEqual(saldo(debitosArray,creditosArray),0)
        self.assertAlmostEqual(debitoGrande(debitosArray),0)

    def test_array3(self):
        debitosArray = [100,90,80,70,60,50,40,30,20,10]
        creditosArray = [50,40,30,20,10]
        self.assertAlmostEqual(totalDebitosf(debitosArray),550)
        self.assertAlmostEqual(totalCreditosf(creditosArray),150)
        self.assertAlmostEqual(promedioDebitos(debitosArray),55)
        self.assertAlmostEqual(saldo(debitosArray,creditosArray),-400)
        self.assertAlmostEqual(debitoGrande(debitosArray),100)

if __name__ == '__main__':
    unittest.main()