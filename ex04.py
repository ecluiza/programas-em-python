agua=0.0
classificacao=""

agua=float(input("Informe a quantidade de pontos na agua: "))

if(agua<=10):
    classificacao="rochosa"
else:
    if(agua>10)and(agua<=40):
        classificacao="firme"
    else:
        if(agua>40)and(agua<=80):
            classificacao="pantanosa"
        else:
            classificacao="quantidade invalida"

print(f"A amostra de agua esta classificada em: {classificacao}")
