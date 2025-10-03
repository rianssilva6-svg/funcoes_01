import os 
os.system("cls")
   
#função com passagem de parametros
# criando uma função
def saudacao(nome, idade, peso, altura):
    print (f"Olá, {nome}! Bem-vindo(a)")
    print (f"Sua idade é {idade} anos")
    print (f"Sua altura é {altura}m")
    print (f"Seu peso é {peso}kg")

#os dados
nome = input("Digite seu nome: ")    
idade = int(input("Digite sua idade: "))    
peso = float(input("Digite sua altura: "))    
altura = float(input("Digite seu peso: "))    
os.system("cls")

#chamando a função
saudacao(nome, idade, peso, altura)