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



