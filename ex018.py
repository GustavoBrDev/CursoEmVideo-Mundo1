import math
angulo = float(input('Qual é o angulo? '))
print(f'''Analisando \033[32m{angulo}\033[m descobrimos:
Que o seu SENO é \033[1;31m{math.sin(math.radians(angulo)):.2f}\033[m
Que o seu COSSENO é \033[1;33m{math.cos(math.radians(angulo)):.2f}\033[m
Que o seu TANGENTE é \033[1;35m{math.tan(math.radians(angulo)):.2f}\033[m''')