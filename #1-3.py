def  Primes(N_list):
  P_list=[]
  #Iteracion de los erlemtos de la lista
  for n in N_list:
    divisors=[] # luista de divisores de cada número 
    for i in range (1, n+1):
      if n%i==0: #Conocer si el número es divisor o no
        divisors.append(i)
    if len(divisors)==2: #Comprobar si es primos
      P_list.append(n)
  return P_list

if __name__=="__main__":
  N_list=[]
  cant=int(input("Ingrese la cantidad de elementos de su lista: "))
  for i in range(cant):
      N_list.append(int(input(" -> ")))

  print("Los números primos de la lista " + str(N_list)+ " son " +str(Primes(N_list)))
