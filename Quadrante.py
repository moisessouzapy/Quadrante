i = 1
while i < 2:
  print("digite um número x: ")
  x = int(input())
  print("digite um número y: ")
  y = int(input())
  i += 1
  if(x > 0 and y > 0):
    print("primeiro quadradnte")
  elif(x < 0 and y > 0):
    print("segundo quadrante")
  elif(x < 0  and y < 0 ):
    print("terceiro quadrante")
  elif(x > 0 and y < 0) :
    print("quarto quadrante")
  else:
    break