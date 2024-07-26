dias = int(input('Quantos \033[36mdias\033[m o carro foi utilizado? '))
km = float(input('Quantos \033[33mkms\033[m foram percorridos? '))
print(f'Com \033[36m{dias}\033[m dias de uso e \033[33m{km}\033[m km percorridos, sua fatura será de \033[32m{dias*60+km*0.15 :.2f}\033[m')