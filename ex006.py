while True:
  try:
   n=int(input('Digite um numero: '))
   print(f'''Analisando \033[1;36m{n}\033[m temos:
   Sua raiz quadrada é \033[31m{n**(1/2):.2f}\033[m
   O dobro de \033[1;36m{n}\033[m é \033[34m{n*2}\033[m
   Enquanto o seu triplo é \033[31m{n*3}\033[m''')
   break
  except:
    print('\033[7;31mO valor não é reconhecido, tente novamente\033[m')