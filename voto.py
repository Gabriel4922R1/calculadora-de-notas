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

candidato = int(input("Digite seu voto: "))
if candidato == 10:
    print("Paulo Freire")
elif candidato == 20:
    print("Jean Piaget")
else:
    print("Candidato não encontrado")
    
