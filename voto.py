print("digite seus documentos para votar ")

rg = int(input("Digite seu RG: "))
if rg == 12345678:
    print("RG Correto")
else:
        print("RG Incorreto ")
titulo = int(input("digite o n�mero do seu t�tulo: "))
if titulo == 11122233344:
        print("Ol� Jo�o de Carmo, pode votar!")
else:
        print("Eleitor n�o encontrado")

candidato = int(input("Digite seu voto: "))
if candidato == 10:
    print("Paulo Freire")
elif candidato == 20:
    print("Jean Piaget")
else:
    print("Candidato n�o encontrado")
    
