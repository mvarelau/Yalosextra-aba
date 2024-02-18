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





