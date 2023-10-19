#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
word="caña"#input("ingrese una palabra: ")
for i in range(0,10):
  print(f"{i+1}: {word}")

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age=10#int(input("ingrese su edad: "))
date=2023
end=date-age
age=1
while end!=date:
  print(f"Usted cumplió en {end+1}, {age}")
  end=end+1
  age=age+1
  
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
print("Numeros impares")
n=10#int(input("un número entero positivo"))
for i in range(1,n+1):
  if i%2!=0:
    print(i,end=", ")
print("")

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
print("Cuenta regresiva")
n=5#int(input("un número entero positivo"))
for i in range(n,0,-1):  
  print(i,end=", ")
  
print("")
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

dinero=1000#float(input("Ingrese dinero a invertir: "))
interes=0.25#float(input("Ingrese el interes anual: "))
cantidad_a=4#int(input("Ingrese la cantidad de años: "))
capital=((dinero*interes)+dinero)*cantidad_a
print("Su inversion anual dio un total de: $",capital)
print("")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
n=9#int(input("Ingrese el tamaño del triangulo: "))
for i in range(0,n):
  print("*",end="")
  for j in range(0,i):
    print("*",end="")
  
  print("")
#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
for i in range(1,11):
  print("TABLA DEL ",i)
  for j in range(1,11):
    print(i,"x",j,"=",i*j)
  print("")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1 
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
# 11 9 7 5 3 1...

num=7
count=1

for i in range(0,num):
  if count%2!=0:
    print(count,end=" ")
    regresiva=count
    while regresiva>0:
      regresiva=regresiva-1
      if regresiva%2!=0 and regresiva!=0:
        print(regresiva,end=" ")
      
        
  print("")
  if num%2==0:
    count=count+1
  else:
    count=count+1
    
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña="CD350UP375"
flag=False
while flag==False:
  enter=input("Ingrese la contraseña: ")
  if contraseña!=enter:
    print("Contraseña Incorrecta")
  else:
    print("Correcto")
    flag=True
    
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num=int(input("Ingrese un numero entero: "))
if num%2==0:
  print("Numero primo")
else:
  print("No es numero primo")

#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra=input("Ingrese una palabra: ")
for i in range(0,len(palabra)):
  print(palabra[i],end=" ")

#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
palabra="holas como estas aaa"#input("Ingrese una palabra: ")
letra="h"#input("Ingrese una letra: ")
cont=0
for i in range(0,len(palabra)):
  if palabra[i]==letra:
    cont=cont+1
print(f"la letra {letra} se repite {cont} veces")

#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
flag=False
print("Ingrese 'salida' para salir")
while flag==False:
  entrada=input("Escribe algo: ")
  if entrada=="salir":
    flag=True


#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
n_uno=2#int(input("Ingrese un numero: "))
n_dos=12#int(input("Ingrese otro numero: "))
if n_uno>n_dos:
  mayor=n_uno
  menor=n_dos
else:
  mayor=n_dos
  menor=n_uno

for i in range(menor,mayor+1):
  print(i, end=" ")
  if i%2==0:
    print("es par")
  else:
    print("es impar")
  print("")

#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
num=46#int(input("Ingrese un numero mayor que cero: "))
print("Divisores: ",end="")
for i in range(1,num+1):
  if num%i==0:
    print(i,end=", ")


#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
total=int(input("Ingrese qué cantidad de numeros va a ingresar:"))
cont=0
for i in range(0,total):
  numero=int(input("Ingrese un numero:"))
  if numero<0:
    cont=cont+1
print(f"Se ingresaron {cont} numeros negativos")


#Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
frase="comida de JUeves"#input("Ingrese una frase: ")
frase=frase.lower()
show_V=""
vocales=["a", "e", "i", "o", "u"]
for i in frase:
  if i in vocales and i not in show_V:
    show_V=show_V+i
    print(i,end=" ")
print("")


#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
x=0
y=1
resultado= 1
print(0,end=" ")
for i in range(0,10):
  print(resultado,end=" ")
  resultado=x+y
  x=y
  y=resultado

#Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
mony = 0
meta=int(input("Ingrese la cantidad de dinero que se quiere ahorrar: "))
while mony<=meta:
  entra=int(input("$: "))
  if mony<0:
    print("la cantidad debe ser posiativa!")
  else:
    mony=mony+entra

print(f"Sus ahorros fueron de: {mony}")

#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
suma=0

while True:
  entrada=int(input("Ingrese un número entero: "))
  suma=suma+entrada
  if entrada==0:
    break
print("La suma de los números ingresados es: ",suma)

#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
flag=False
mayor=0
while flag!=True:
  entrada=int(input("Ingrese un número entero positivo: "))
  if entrada<0:
    print("Ingrese un número entero positivo")
  else:

    if entrada>mayor:
      mayor=entrada
    if entrada==0:
      flag=True
print("El mayor número ingresado fue: ",mayor)


#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
flag=False
suma=0
while flag!=True:
  monto=int(input("Ingrese el monto de la compra: "))
  if monto==0:
    flag=True
  else:
    if monto<0:
      print("Ingrese un monto positivo: ")
    else:
      suma=suma+monto

if suma>1000:
  print("Usted ha obtenido un descuento!")
  total=suma-(suma*0.10)
  print("El total a pagar es: ",total)
else:
  print("El monto es: ",suma)



#Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

n=int(input("Ingrese un valor: "))
if n>0:
  x=1
  fac=1
  while x<=n:
    fac=fac*x
    x=x+1
  print("El factorial de",n,"es",fac)
else:
  if n==0:
    print("El factorial de",n,"es",1)