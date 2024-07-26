metros = float(input('Digite um valor: '))
print(f'O valor \033[37m{metros}\033[m corresponde a:\n'
      f'\033[37m{metros}\033[m metros\n'
      f'\033[1;31m{metros / 1000}\033[m km\n'
      f'\033[1;32m{metros / 100}\033[m hectoremtro(s)\n'
      f'\033[1;33m{metros / 10}\033[m\n'
      f'\033[1;34m{metros * 10 :.0f}\033[m decimetro\n'
      f'\033[1;35m{metros * 100 :.0f}\033[m centimetros\n'
      f'\033[1;36m{metros * 1000 :.0f} \033[mmilimetros')