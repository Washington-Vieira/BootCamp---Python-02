
CONSTANTE_BONUS = 1000
# 1- Solicite ao usuário que digite o seu nome
nome_usuario = input("Digite o seu nome: ")

# 2 - Solicite ao usuário que digite o valor do seu salário
# converta a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o seu salario: "))

# Solicite ao usuário que digite o valoor do bónus recebido
# converta a entrada para número de ponto flutuante

bonus_usuario = float(input("Digite o seu bonus: "))

# Calcule o valor do bonus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# Imprima a mensagem personalisada para o usuario incluindo o nome e o valor do bonus

#print f para misturar texto com variaveis 
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")
