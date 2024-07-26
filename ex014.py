graus = float(input('Informe a temperatura em ºC:'))
if graus >= 30:
    print(f'A temperatura \033[31m{graus:.1f}ºC\033[m  corresponde a \033[32m{graus *9 /5 +32:.1f}ºF\033[m')
elif graus >=15:
    print(f'A temperatura \033[33m{graus:.1f}ºC\033[m corresponde a \033[32m{graus *9 /5 +32:.1f}ºF\033[m')
else:
    print(f'A temperatura \033[36m{graus:.1f}ºC\033[m  corresponde a \033[32m{graus *9 /5 +32:.1f}ºF\033[m')