km = float(input('Quantos km tem sua viagem? '))
if km <= 200:
    print(f'O valor da sua viagem é de \033[1;32mR${km * 0.50:.2f}\033[m')
else:
    print(
      f'Com o \033[1;36mdesconto\033[m para viagens longas, o valor da sua viagem será de \033[1;32mR${km * 0.45:.2f}\033[m')
