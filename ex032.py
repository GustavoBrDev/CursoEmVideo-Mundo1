from datetime import date

print('Utilize \033[4;34m0\033[m para analisar o \033[1;33mano atual\033[m do seu computador')
ano = int(input('Digite o \033[33mano\033[m a ser analisado: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;32m{ano} é\033[m um ano \033[1;36mBISSEXTO\033[m')
else:
    print(f'\033[1;31m{ano} NÃO\033[m é um ano \033[1;36mBISSEXTO\033[m')
