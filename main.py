def es_par(numero):
  """Retorna True si el número es par, o False si es impar."""
  return numero % 2 == 0

n = 1000
print("start")
for x in range(0, n):
  print(x,es_par(x))  # True if x is even, False if x is odd
print("end")