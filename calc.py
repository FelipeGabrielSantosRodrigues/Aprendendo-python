print("Subtração:1")
print("Multiplicação:2")
print("Divisão:3")
print("Soma:4")

while True:

  
  tipo = input("Escolha A Operação:")
  
  if tipo == "1":
  
   subtração = input("Digite Um Valor: ")
   subtração = int(subtração)

   gasto1 = input("Quanto Deseja Subtrair ?: ")
   gasto1 = int(gasto1)
  
   resultado = subtração - gasto1

   print("Total:",resultado)
  

   repetir = input("Quer fazer outro cálculo? (s/n): ").lower()
   
   if repetir != "s":
      print("Encerrando o programa...") 
      break


  if tipo == "2":
    
     multiplicação = input("Digite Um Valor: ")
     multiplicação = int(multiplicação)

     gasto2 = input("Quanto Deseja Multiplicar ?: ")
     gasto2 = int(gasto2)

     resultado = multiplicação * gasto2

     print("Total:",resultado)

     repetir = input("Quer fazer outro cálculo? (s/n): ").lower()
     if repetir != "s":
      print("Encerrando o programa...") 
      break



  
  if tipo == "3":
    
     divisão = input("Digite Um Valor: ")
     divisão = float(divisão)

     gasto3 = input("Quanto Deseja Dividir ?: ")
     gasto3 = int(gasto3)

     resultado = divisão / gasto3

     print("Total:",resultado)


     repetir = input("Quer fazer outro cálculo? (s/n): ").lower()
     if repetir != "s":
      print("Encerrando o programa...") 
      break
     
  
  if tipo == "4":
  
     soma = input("Digite Um Valor: ")
     soma = int(soma)

     gasto4 = input("Quanto Deseja Adicionar ?: ")
     gasto4 = int(gasto4)
  
     resultado = soma + gasto4

     print("Total:",resultado)
  

     repetir = input("Quer fazer outro cálculo? (s/n): ").lower()
   
     if repetir != "s":
      print("Encerrando o programa...") 
      break