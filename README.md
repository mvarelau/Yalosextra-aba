# Yalosextra-aba
Reto #1 POO
## Punto 1
* Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
```python
def basic_operations(a:float,b:float,operation):
    #Determinar la operacion que se hará
    if operation == "+":
        print("La suma de "+ str(a)+ " y " + str(b)+ " es: " + str(a+b))
    elif operation == "-":
        print("La resta de "+ str(a)+ " y " + str(b)+ " es: " + str(a-b))
    elif operation == "*":
        print("La multiplicación de "+ str(a)+ " y " + str(b)+ " es: " + str(a*b))
    elif operation== "/":
        print("La división de "+ str(a)+ " y " + str(b)+ " es: " + str(a/b))
    elif operation == "Todas":
      print("Suma: "+ str(a+b)+ "\nResta: " + str(a-b)+ "\nMultiplicación:"+ str(a*b)+ "\nDivisión: "+str(a/b))

if __name__=="__main__":
    #Definición de variables
    a=(input("Ingrese un número real: "))
    b=(input("Ingrese un número real: "))
    list_=["1","2","3","4","5","6","7","8","9","0"]
    l_operations=["+","-","*","/", "Todas"]
   #Programa anti tontos
    while a not in list_ or b not in list_:
        print("Ingrese dos números validos.")
        a:float=(input("Ingrese un número real: "))
        b:float=(input("Ingrese otro número real: "))
    operation=(input("Qué operación decea hacer entre estos dos númereos:\nIngrese + para hacer la suma\nIngrese - para hacer la resta\nIngrese * para hacer la múltiplicación\nIngrese / para hacer la división\nIngrese'Todas' para hacer todos. "))
    while operation not in l_operations:
      operation=input("Ingrese una operación válida")
    # a y b quedan guardaqdos como str asi que los convierto a float
    a=float(a)
    b=float(b)
    basic_operations(a,b,operation)


```
## Punto 2
* Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
```python
def palindrome(W_list):
  position= len(W_list)-1
  for v in W_list:
    #juego de posiciones simetricas para saber si la palabra es palíndroma
    if W_list[W_list.index(v)] == W_list[position-W_list.index(v)]:
      print_= "La palabra es palindroma"
    else:
      print_="La palabra no es palindroma"
  print(print_)

if __name__=="__main__":
  word:str=(input("Ingrese una palabra para conocer si es palíndorma o no: ") )
  #Convertir palabra en lista para jugar con las posiciones
  W_list= list(word)
  palindrome(W_list)
```
## Punto 3
* Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```python
def  Primes(N_list):
  P_list=[]
  for n in N_list:
    divisors=[]
    for i in range (1, n+1):
      if n%i==0:
        divisors.append(i)
    if len(divisors)==2:
      P_list.append(n)
  return P_list

if __name__=="__main__":
  N_list=[]
  cant=int(input("Ingrese la cantidad de elementos de su lista: "))
  for i in range(cant):
      N_list.append(int(input(" -> ")))

  print("Los números primos de la lista " + str(N_list)+ " son " +str(Primes(N_list)))
```
## Puno 4
* Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python
def biggest_addition(N_list):
    long_ = len(N_list) - 1
    A_list = []
    counter = 0
    while counter < long_:
        n = N_list[counter] + N_list[counter + 1]
        A_list.append(n)
        counter += 1
    biggest = max(A_list)
    return biggest

if __name__ == "__main__":
    N_list = []
    cant = int(input("Ingrese la cantidad de elementos de su lista: "))
    for i in range(cant):
        N_list.append(int(input(" -> ")))
    print(str(N_list))

    print("La suma más grande de elementos consecutivos es: " + str(biggest_addition(N_list)))
```
## Punto 5
* Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
 ```python
def letters(W_list):
    Ord_list = []

    counter = 0
    while counter < len(W_list):
        count_1 = counter + 1
        while count_1 < len(W_list):
            # Convertir las palabras en listas de caracteres y ordenarlas
            sorted_word1 = sorted(list(W_list[counter]))
            sorted_word2 = sorted(list(W_list[count_1]))
            
            # Verificar si las palabras tienen los mismos caracteres
            if sorted_word1 == sorted_word2:
                Ord_list.append(W_list[counter])
                Ord_list.append(W_list[count_1])
            count_1 += 1
        counter += 1
    
    return Ord_list

if __name__ == "__main__":
    W_list = []
    cant = int(input("Ingrese la cantidad de elementos de su lista: "))
    for i in range(cant):
        W_list.append(str(input(" -> ")))
    print(str(letters(W_list)))
```
