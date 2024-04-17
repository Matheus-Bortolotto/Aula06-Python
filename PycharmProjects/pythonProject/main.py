# --------------------------1 ------------------

# nota = int(input('Diga uma nota entre 1 a 10: '))
# while nota > 10:
#     nota = int(input('digite novamente: '))
# print('parabens')
#
# corrercao
# while True:
#     num=input('diga um numero entre 0 e 10: ')
#     if num.isnumeric():
#         num = int(num)
#         if num >= 0 and num <=10:
#             break
#         else:
#             print('deve ser um numero entre 0 e 10')
#     else:
#         print('isso nao e um numero')

#
# -----------------------------EXERCICIO 2 ----------------
# nome = input('diga seu nome: ')
# while len(nome) <= 3:
#     print('precisa ter mais de 3 caracteres')
#     nome = input('digite seu nome: ')
# idade = int(input('diga sua idade: '))
# while idade > 150:
#     print('voce precisa ter entre 1 e 150 anos')
#     idade = int(input('digiye sua idade: '))
# salario = int(input('diga seu salario: '))
# while salario < 0:
#     print('digite outro valor: ')
#     salario = input('digite seu salario verdadeiro: ')
# sexo = input("Digite o seu sexo 'f' ou 'm': ")
# while sexo == "f" and "m" :
#     print("Digite um sexo válido (f ou m)!")
#     sexo = input("Digite o seu sexo 'f' ou 'm': ")
# estado = input("Digite o seu estado civil 's', 'c', 'v' ou 'd': ")
# while  estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
#     print("Digite um estado válido: (s, c, v ou d)!")
#     estado = input("Digite o seu estado civil 's', 'c', 'v' ou 'd': ")

# correcao

# nome = input('diga seu nome: ')
# while len(nome) <= 3:
#     print('precisa ter mais de 3 caracteres')
#
# while True:
#     num=input('diga um numero entre 0 e 10: ')
#     if num.isnumeric():
#         num = int(num)
#         if num <=150:
#             break
#         else:
#             print('deve ser um numero entre 0 e 150')
#     else:
#         print('isso nao e um numero')
#
# salario = input('diga seu salario: ')
# while not salario.isnumeric():
#     print('diga um numero')
#     salario = input('diga seu salario: ')
#
# sx = input('diga f ou m')
# while sx != 'f' and sx != 'm': # not (sx == 'f' or sx == 'm')
#     sx = input('diga apenas f ou m')
#
# ec = input('diga seu estado civil (s,c,v,d: ')
# while ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
#     ec = input('diga seu estado civil (s,c,v,d: ')

# -------------------------EXERCICIO 3 ----------------------
#
# populacaoA = 80000
# populacaoB = 200000
# ano = 0
#
# while populacaoA < populacaoB:
#     populacaoA += (populacaoA * 3) / 100
#     populacaoB += (populacaoB * 1.5) / 100
#     ano += 1
# print(f"Serão necessários {ano} anos")
#
# correcao

# correcao
# a = 80
# b = 200
# t = 0
# while a  < b:
#     a*=1.03
#     b*=1.015
#     t+=1
# print(t)

#
# --------------------------------EXERCICIO 4 ------------------
# i = 1
# soma = 0
# while i <= 5 :
#     valor = float(input(f"Diga o {i}° valor: "))
#     soma += valor
#     media = soma /2
#     i += 1
# print(f'a soma dos numeros é {media}')

# CORRECAO

# i = 0
# soma = 0
# while i < 5:
#     num = input(f"Diga o {i+1}° valor: ")
#     while not num.isnumeric():
#         print('deve ser um numero: ')
#         num = input(f"Diga o {i+1}° valor: ")
#     num = int(num)
#     soma += num
#     i += 1
# print(f'a soma é {soma} e a media é {soma/i}')

#
# -------------------------EXERCICIO 5 -------------------
# num1 = int(input("digite um numero: "))
# num2 = int(input("digite outro numero: "))
# if num1 > num2 :
#     num1 = num2
# while num1 < num2 - 1:
#     num1 += 1
#     print(num1)

# CORRECAO
# a = int(input('diga um numero: '))
# b = int(input('diga outro numero: '))
# while a < b:
#     print(a)
#     a+=1
# while b < a:
#     print(b)
#     b+=1

# ------------------------EXERCICIO 6 -------------------------
# nome = input('diga seu nome: ')
# senha = input('digite uma senha: ')
# while nome == senha:
#     print('o nome e a senha nao podem ser iguais')
#     nome = input('diga seu nome: ')
#     senha = input('diga sua senha: ')
# print(f'seja bem vindo {nome}')

# -----------------------EXERCICIO 7 ---------------------
# n = int(input('qual tabuada voce deseja: '))
# if n < 1 or n > 10:
#     print('digite um numero entre 1 e 10')
#     n = int(input('qual tabuada voce deseja: '))
# else:
#     print(f'a tabuado de {n} é: ')
#     contador = 1
#     while contador <= 10:
#         resultado = n * contador
#         print(f'{n} X {contador} = {resultado}')
#         contador += 1

# CORRECAO

# num = 1
# while num <= 10:
#     i = 1
#     print(f'tabuada do {num}')
#     while i <= 10:
#         print(f'{num} * {i} = {num * i}')
#         i += 1
#     num += 1
#     print()

# -----------------------EXERCICIO 8 -----------------------
# n = int(input("Digite o numero que deseja gerar: "))
# if n <=0:
#     print("Numero invalido. Digite um numero maior que zero")
# else:
#     primeiro_termo = 1
#     segundo_termo = 1
#     contador = 2
#     print(f"serie ate o {n} termo")
#     print(primeiro_termo)
#     print(segundo_termo)
#     while contador < n:
#         prximo_termo = primeiro_termo + segundo_termo
#         print(prximo_termo)
#         primeiro_termo = segundo_termo
#         segundo_termo = prximo_termo
#         contador += 1
#CORRECAO
# primeiro_soma = 1
# print(primeiro_soma, end=' ')
# segunda_soma = 1
# print(segunda_soma, end=' ')
# qtd = 17
# i = 2
# while i < 17:
#     terceira_soma = primeiro_soma + segunda_soma
#     print(terceira_soma,end=' ')
#     primeiro_soma = segunda_soma
#     segunda_soma = terceira_soma
#     i += 1

# --------------------- EXERCICIO 9 ------------------
# par = 0
# impar = 1
# contador = 0
# while contador < 10:
#     numero = int(input(f"Diga o {contador}° valor: "))
#     if numero % 2 == 0:
#         par += 1
#     else:
#         impar += 1
#     contador += 1
# print(f' pares {par}')
# print(f'impar {impar}')

# ----------------------- EXERCICIO 10 ---------------------
# numero = int(input("Fatorial de: ") )
#
# resultado=1
# count=1
#
# while count <= numero:
#     resultado *= count
#     count += 1
#
# print(resultado)
# CORRECAO
# num = 5
# fatorial = num
# fatorial_print = f'{num}! =  '
# while num > 1:
#     fatorial_print += f'{num} *'
#     num -= 1
#     fatorial *= num
# fatorial_print += '1'
# print(f'{fatorial_print} = {fatorial}')

# ------------------------- EXERCICIO 11 ----------------------
# numero = int(input("Digite um numero: "))
#
# if numero < 2:
#     print(f"{numero} nao e primo.")
# else:
#     primo = True
#     for i in range(2, numero):
#         if numero % i == 0:
#             primo = False
#             break
#     if primo:
#         print(f"{numero} é primo")
#     else:
#         print(f"{numero} nao é primo.")
# CORRECAO
# num = 7
# i = 2
# while i < num:
#     print(f'{num}%{i} = {num%i}')
#     if num %i==0:
#         print(f'{num} nao e primo')
#         break
#     i += 1
# if i == num**0.5:
#     print(f'{num} é primo')

# ---------------12--------------- nao feitos
# n = int(input("Digite a quantidade"))
# i = 0
# soma = 0
# while i < n:
#     num = input(f"Diga o {i+1}° valor: ")
#     while not num.isnumeric():
#         print('deve ser um numero: ')
#         num = input(f"Diga o {i+1}° valor: ")
#     num = int(num)
#     soma += num
#     i += 1
# print(f'a soma é {soma} e a media é {soma/i}')
# ----------------13-----------------
# final = 2024
# salario = 1000
# taxa = 0.015
# partida =  1995
# while partida < final:
#     salario *= (1+taxa)
#     taxa *= 2
#     partida +=1
# print(salario)
# ------------------------14---------------------
# primeiro = 0
# segundo = 0
# terceiro = 0
# quarto = 0
# while True:
#     num = int(input("Diga um numero"))
#     if num <0:
#         break
#     if num < 25:
#         primeiro += 1
#     elif num <= 50:
#         segundo += 1
#     elif num <=75:
#         terceiro += 1
#     elif num <=100:
#         quarto +=1
# ------------------15----------------
# joao = 0
# jose = 0
# joana = 0
# jorel = 0
# nulo = 0
# branco =0
# i = 0
# while True:
#     num = input("Diga o seu voto: \n 1 -João\n 2- Jose \n 3 - Jorel\n4 - Joana\n5 - Nulo\n6- Branco\n0 - sair")
#     while num != "0" and num != "1" and num != "2" and num != "3" \
#             and num != "4" and num != "5" and num != "6":
#         num = input("Diga o seu voto: \n 1 -João\n 2- Jose \n 3 - Jorel\n4 - Joana\n5 - Nulo\n6- Branco\n0 - sair")
#     if num == "0":
#         break
#     elif num =="1":
#         joao +=1
#     elif num =="2":
#         jose +=1
#     elif num =="3":
#         jorel +=1
#     elif num =="5":
#         joana +=1
#     elif num =="5":
#         nulo +=1
#     elif num =="6":
#         branco +=1
# print(f"Joao: {joao}\nJose: {jose}\nJorel: {jorel}\nJoana: {joana}"
#       f"\nNulos: {nulo/i:.2f}%\nBrancos: {branco/i:.2f}%")
i = 0
while i <10:
    num = int(input("Diga um numeoro"))
    if num % 2 ==0:
        print(f"{num} é par ")
        continue
    print(f"{num} é impar")













# numero = int(input("digite um numero entre 1 e 10"))
# if numero < 1 or numero > 10:
#     print("Numero invalido. Digite um numero entre 1 e 10")
# else:
#     print(f"tabuada de {numero}: ")
#     contador = 1
#     while contador <= 10:
#         resultado = numero * contador
#         print(f"{numero} x {contador} = {resultado}")
#         contador += 1
#
# num = 1
#
# while num <= 10:
#     i =1
#     while i <= 10:
#         print(f"{num} *{i}={num * i }")
#         i += 1
#     num +=1


