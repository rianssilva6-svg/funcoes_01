import os 
os.system("cls")

def logo_senai():
    os.system("cls")
    print("========")
    print("= SENAI =")
    print("========")

logo_senai()
nome = input("Digite seu nome: ")

logo_senai()
idade = int(input("Digite sua idade: "))

logo_senai()
peso = float(input("Digite o peso: "))

logo_senai()
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"peso: {peso}kg")