crianca= (0, 12)
adolescente = (13, 17)
adulto = (18, 59)                    #lembrar-se do indice de tupla!!!!
idoso = (60, 120)
idade = int(input("Digite a sua idade: "))
#calculo de idade
if idade >= crianca[0] and idade <= crianca[1]:                                    
    print ("Voce e uma criança")
elif idade >= adolescente[0] and idade <= adolescente[1]:
    print ("Voce e um adolescente")
elif idade >= adulto[0] and idade <= adulto[1]:
    print ("Voce e um adulto")
elif idade >= idoso[0] and idade <= idoso[1]:
    print ("Voce e um idoso")
#fim codigo