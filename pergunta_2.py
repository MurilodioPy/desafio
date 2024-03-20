def verifica_fibonacci(n):
  x = 0
  y = 1
  for i in range(n + 1):
    z = x + y
    if z == n:
      return "Número pertence a sequência de Fibonacci!"
    elif i == n:
      return "Número NÃO pertence a sequência de Fibonacci!"
    y = x
    x = z

print(verifica_fibonacci(4181)) # Número pertence a sequência de Fibonacci!