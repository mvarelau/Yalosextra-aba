def biggest_addition(N_list):
    long_ = len(N_list) - 1
    A_list = []# Lista en la que se agregran todas las sumas 
    counter = 0
    #iteracion con los npumeros consecutivos
    while counter < long_:
        n = N_list[counter] + N_list[counter + 1]
        A_list.append(n)
        counter += 1
    biggest = max(A_list) # Se define la suma más grandes
    return biggest

if __name__ == "__main__":
    N_list = []
    cant = int(input("Ingrese la cantidad de elementos de su lista: "))
    for i in range(cant):
        N_list.append(int(input(" -> ")))
    print(str(N_list))

    print("La suma más grande de elementos consecutivos es: " + str(biggest_addition(N_list)))
