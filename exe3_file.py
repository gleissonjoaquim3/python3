arquivo = open("arquivo.txt", "w")
print(arquivo.readable())

arquivo.write("Essa é a primeira linha escrita de texto escrita em python. \n")
arquivo.write("Feita por mim !! Gleisson !!")
arquivo.write("Essa deveria ser a terceira linha porém ainda é a segunda. \n")
arquivo.write("Essa sim é a terceira.")

arquivo.close()

arquivo = open("arquivo.txt", "r")
print(arquivo.readable())
print(arquivo.read())

arquivo.close()
