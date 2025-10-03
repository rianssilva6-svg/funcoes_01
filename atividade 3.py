import os
os.system("cls")

#função
def positivo_e_negativo (numero):
    print (f"O número escolhido foi {numero}")
    if numero < 0:
        print (f"O número {numero} é negativo")
    elif numero == 0:
        print (f"O numéro {numero} é neutro")    
    else:
        print (f"O número é positivo")

#desenvolvendo
numero = int(input("Digite um número: "))    

#chamando a função
positivo_e_negativo(numero)       