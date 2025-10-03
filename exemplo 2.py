import os
os.system("cls")

#função
def impar_e_par(numero):
    print(f"Número informado foi {numero}")

#desenvolvendo
numero = int(input("Digite um número: "))  

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar")    

#chamando a função
impar_e_par(numero)