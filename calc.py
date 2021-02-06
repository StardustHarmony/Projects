print("Calculadora da Alícia para a lista 1 de PC; Excercício 1 (análise de limites)")
def calc():
  x=float(input("valor: "))
  if x==2:
  	print("indeterminação. Denominador=0")
  else:
    x=(x**2-2*x)/(x**2-x-2)
  print(x)
  calc()

calc()