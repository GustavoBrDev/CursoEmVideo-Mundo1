money = float(input('Qual é o salário do funcionário? R$'))
print(f'O funcionário que recebia \033[32mR${money:.2f}\033[m, com \033[33m15%\033[m de aumento , passa a receber \033[32mR${money+(money*15/100):.2f}\033[m')