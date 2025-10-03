import os
os.system ("cls")

#funções

def nota (media):
    if media >=7:
        print(f"Aluno aprovado, média: {media}")
    else:
        print(f"Aluno reprovado, média: {media}")

#desenvolvendo  
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

#mostrando a função
nota(media)