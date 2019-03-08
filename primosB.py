res=0
i=0
a=int(input("Ingresa el numero:"))
while i<=a:
  i=i+1
  if a%i==0:
    res=res+1
if res>2:
 print("no es un numero primo")
else:
 print("es primo")