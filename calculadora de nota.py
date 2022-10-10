nota_1 = int(input ("Digite a nota 1"))
nota_2 = int(input ("Digite a nota 2"))
nota_3 = int(input ("Digite a nota 3"))
nota_4 = int(input ("Digite a nota 4"))
total = nota_1 + nota_2 + nota_3 + nota_4
média = total / 4
print ("nota total: ", total, "média: ", média)
if média < 6.0:
    print("reprovado")
if média >= 6.0:
    print("aprovado")