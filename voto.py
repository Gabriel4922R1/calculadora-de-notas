Paulo_Freire = 0

Jean_Piaget = 0

print("digite seus documentos para votar ")

rg = int(input("Digite seu RG: "))
if rg == 12345678:
    print("RG Correto")
else:
        print("RG Incorreto ")
titulo = int(input("digite o número do seu título: "))
if titulo == 11122233344:
        print("Olá João de Carmo, pode votar!")
else:
        print("Eleitor não encontrado")

print("Paulo Freire = 10 ")
print("Jean Piaget = 20 ")

voto = int(input("Digite seu voto: "))

if voto == 10:
    Paulo_Freire += 1

else:
    Jean_Piaget +=1

print(f"Candidato Paulo Freire tem: {Paulo_Freire} votos, Candidato Jean_Piaget tem: {Jean_Piaget} votos")