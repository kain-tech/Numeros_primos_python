def eh_primo(n):
  #verifica se o numero é menor que 2
  if(n <= 1):
    return False

  #verifica se o numero é 2, que é o unico numero par primo
  if(n == 2):
    return True

  #verifica se o numero par é maior que 2
  if(n % 2 == 0):
    return False

  #verifica divisores de 3 até raiz quadrada de n
  raiz_quadrada = int(n**0.5) + 1
  for i in range(3, raiz_quadrada, 2):
    if n % i == 0:
      return False
  return True

#testa a função com exemplos
numeros_teste = [10, 92, 83, 74, 56]
for numero in numeros_teste:
  if eh_primo(numero):
    print(f"{numero} é primo.)
  else:
    print(f"{numero} não é primo.)
