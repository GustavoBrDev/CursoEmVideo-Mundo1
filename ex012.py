teste = float(input('Qual é o preço do produto? R$'))
print(f'Com uma promoção de \033[33m5%\033[m, o preço do produto ficará: \033[32mR${teste-(teste*5/100):.2f}\033[m')