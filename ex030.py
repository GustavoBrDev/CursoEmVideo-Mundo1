num = int(input('Digite um numero qualquer: '))
print('=' * 20)
if num % 2 == 0:
    print(f'O numero {num} é \033[32mPAR\033[m.')
else:
    print(f'O numero {num} é \033[34mÍMPAR\033[m')
print('=' * 20)

