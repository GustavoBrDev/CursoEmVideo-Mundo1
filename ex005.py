while True:
  try:
   n=int(input('Digite um numero inteiro '))
   depois=n+1
   antes=n-1
   print(f'''Analisando o valor \033[36m{n}\033[m temos:
   O seu antecessor é \033[33m{antes}\033[m
   O seu sucessor é \033[35m{depois}\033[m''')
   break
  except:
    print('\033[7;31mO valor não é valido, insira um numero inteiro\033[m')