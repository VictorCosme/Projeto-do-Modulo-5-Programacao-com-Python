# MENU DE NAVEGAÇÃO
print("Sê bem-vindo(a)!")
print(" ")
print("Por favor, escolha uma das questões abaixo:")
print("1. Soma de três números;")
print("2. Quadrilha;")
print("3. Antecessor e Sucesssor;")
print("4. Par ou Ímpar;")
print("5. Calculadora Simples;")
print("6. Idade em Dias")
print("7. Menor e Maior de 3 Números")
print("8. Fatorial")
print("9. Média da Sequência")
# (...)
print("")
questao = int(input("Digite: "))
print("----------------------------------------------")

#QUESTÃO 1 - SOMA DE TRÊS NÚMEROS
if questao == 1:
  print("Escolheste Soma de três números!")
  print(" ")

  num1 = int(input("Digite o primeiro número inteiro: "))
  num2 = int(input("Digite o segundo: "))
  num3 = int(input("E agora o terceiro: "))
  soma = num1 + num2 + num3

  print(" ")
  print("A soma dos números é", soma)

# QUESTÃO 2 - QUADRILHA
if questao == 2: 
  print("Escolheste Quadrilha!")
  print(" ")
  
  homem1 = input("Digite um nome masculino: ")
  mulher1 = input("Agora, um feminino: ")
  homem2 = input("E outro masculino: ")
  mulher2 = input("E feminino: ")
  homem3 = input("Masculino novamente: ")
  mulher3 = input("Feminino outra vez: ")
  homem4 = input("E, por fim, outro masculino: ")
  print(" ")
  print(homem1 + " amava " + mulher1 + " que amava " + homem2)
  print("que amava " + mulher2 + " que amava " + homem3 + " que amava " + mulher3)
  print("que não amava ninguém.")
  print(homem1 + " foi para os Estados Unidos, " + mulher1 + " para o convento,")
  print(homem2 + " morreu de desastre, " + mulher2 +" ficou para a tia,")
  print(homem3 + " suicidou-se e " + mulher3 + " casou com " + homem4)
  print("que não tinha entrado na história.")

#QUESTÃO 3 - SUCESSOR E ANTECESSOR
if questao == 3:
  print("Escolheste Sucessor e Antecessor!")
  print(" ")

  numero_do_pedido = int(input("Qual o númedo do pedido? "))
  antecessor = numero_do_pedido - 1
  sucessor = numero_do_pedido + 1

  print(" ")
  if numero_do_pedido == 1:
    print("O sucessor do pedido", numero_do_pedido, "é", sucessor)
  else: 
    print("O antecessor do pedido", numero_do_pedido, "é", antecessor)
    print("O sucessor do pedido", numero_do_pedido, "é", sucessor)

#QUESTÃO 4 - PAR OU ÍMPAR
if questao == 4:
  print("Escolheste Par ou Ímpar!")
  print(" ")

  numero = int(input("Digite um número inteiro: "))

  print(" ")
  if numero % 2 != 0:
    print("ÍMPAR")
  else:
    print("PAR")

#QUESTÃO 5 - CALCULADORA SIMPLES
if questao == 5:
  print("Escolheste Calculadora Simples!")
  print(" ")

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo: "))
  operacao = input("Escolha uma operação (+, -, *, /): ")

  if operacao == "+":
    print(num1 + num2)

  if operacao == "-":
    print(num1 - num2)

  if operacao == "*":
    print(num1 * num2)

  if operacao == "/":
    if num2 == 0:
        print("Não se pode dividir por 0")
    else:
      print(num1 / num2)

#QUESTÃO 6 - IDADE EM DIAS
if questao == 6:
  print("Escolheste Idade em Dias!")
  print(" ")

  entrada = int(input("Digite a quantidade de dias: "))
  dias = entrada
  meses = 0
  anos = 0

  while dias >= 30:
    dias = dias - 30
    meses = meses + 1

  while meses >= 12:
    meses = meses - 12
    anos = anos + 1

  print(" ")
  print(entrada, "dia(s) <=>", anos, "ano(s),", meses, "mes(es) e", dias, "dia(s)")

#QUESTÃO 7 - MENOR E MAIOR DE 3 NÚMEROS
if questao == 7:
  print("Escolheste Menor e Maior de 3 Números!")
  print(" ")

  a = float(input("Digite um número: "))
  b = float(input("Digite outro: "))
  c = float(input("E agora mais outro: "))
  menor = 0
  maior = 0

  if a <= b and a <= c:
    menor = a
    if b >= c:
      maior = b
    else:
      maior = c

  if b <= a and b <= c:
    menor = b
    if a >= c:
      maior = a
    else:
      maior = c

  if c <= a and c <= b:
    menor = c
    if b >= a:
      maior = b
    else:
      maior = a

  print(" ")
  print(menor, "é o menor dos 3 números")
  print(maior, "é o maior dos 3 números")

#QUESTÃO 8 - FATORIAL
if questao == 8:
  print("Escolheste Fatorial!")
  print(" ")

  n = int(input("Digite um número natural: "))
  fatorial = n

  if n < 0:
    fatorial = "você precisa digitar um número natural"

  if n == 0:
    fatorial = 1

  if n > 0:
    while n > 1:
      n = n - 1
      fatorial = fatorial * n

  print(" ")
  print(fatorial)

#QUESTÃO 9 - MÉDIA DA SEQUÊNCIA
if questao == 9:
  print("Escolheste Média da Sequência!")
  print(" ")
  print("Digite os números para calcular a media. Quando terminar, digite '0'")
  print("")

  entrada = float(input("Digite: "))
  soma = 0
  contador = 0

  while entrada != 0:
    soma = soma + entrada
    contador = contador + 1
    entrada = float(input("Digite: "))

  media = soma / contador
  print("A média é: {:2.2f}".format(media))



#implementar uma opção para voltar ao começo para selecionar outra questão
# Se, no menu, escolherem questao < 1 OU questa > 10, indicar que a opção é inválida