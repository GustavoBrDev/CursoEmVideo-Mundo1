salario = float(input('Qual é o \033[1;32msalário\033[m do funcionário? R$'))
aumento = 15 / 100
if salario > 1250:
    aumento = 10 / 100
print(
    f'Com o aumento de \033[1;33m{aumento * 100:.0f}%\033[m, o \033[1;35msalário\033[m do funcionário será de \033[1;32mR${salario + salario * aumento:.2f}\033[m')
