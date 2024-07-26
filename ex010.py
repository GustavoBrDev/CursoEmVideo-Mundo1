money = float(input('Quanto dinheiro você possui? R$'))
print(f'Com os \033[32mR${money:.2f}\033[m que você possui, você pode comprar:\'\n'
      f'\033[1;34mUS${money / 5.37:.2f}\033[m\n'
      f'\033[1;35m€{money / 6.54:.2f}\033[m')