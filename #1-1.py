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


