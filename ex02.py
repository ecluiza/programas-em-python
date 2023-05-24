precofab=0.0
lucrod=0.0
imposto=0.0
precofin=0.0
percent_imp=0.0
percent_dist=0.0

precofab=float(input("Informe o preço de fabrica: "))
lucrod=float(input("Informe o lucro do distribuidor: "))
imposto=float(input("Informe o valor do imposto: "))

percent_imp=precofab*imposto/100
percent_dist=precofab*lucrod/100

precofin=precofab+percent_dist+percent_imp

print(f"O valor correspondente ao lucro do distribuidor é: {percent_dist:,.2f}")
print(f"O valor correspondente ao imposto é: {percent_imp:,.2f}")
print(f"O preço final do veiculo é: {precofin:,.2f}")



