'''faca um programa que receba o salario base de um funcionario, calcule e mostre o salario a receber, sabendo que esse funcionario 
tem gratificacao de 50,00 e paga imposto de 10% sobre o salario base'''

salariob=0.0
salariof=0.0
imposto=0.0

salariob=float(input("Informe o salario base: "))
imposto=salariob*10/100
salariof=salariob-imposto+50

print(f"O salario a receber é: {salariof}")



