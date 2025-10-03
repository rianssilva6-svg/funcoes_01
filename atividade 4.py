import os
import time
os.system("cls")

#função
def calcular(numero):
    print("===Calculando===")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")    
        time.sleep(1)

#desenvolvendo
numero = int(input("Digite um número para a tabuada: "))

#chamando a função
calcular(numero)
print("Encerrando...")

