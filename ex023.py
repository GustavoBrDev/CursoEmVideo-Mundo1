num=int(input('Informe um \033[43mnumero\033[m:'))
print(f'Unidade:{num//1%10}')
print(f'Dezena:{num//10%10}')
print(f'Centena:{num//100%10}')
print(f'Milhar:{num//1000%10}')