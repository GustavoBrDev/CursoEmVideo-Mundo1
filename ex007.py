n1=float(input('Primeira nota do aluno: '))
n2=float(input('Segunda nota do aluno: '))
media = (n1+n2) /2;

if media == 10:
    print(f'A média do aluno é \033[32m{media:.1f}\033[m')
elif media >=7:
    print(f'A média do aluno é \033[36m{media:.1f}\033[m')
else:
    print(f'A média do aluno é \033[31m{media:.1f}\033[m')