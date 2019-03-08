res=0
a=int(input("Ingresa el numero:"))
for i in range (1,a+1,1):
  if a%i==0:
    res=res+1
if res>2:
 print("no es un numero primo")
else:
 print("es primo")