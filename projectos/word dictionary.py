from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Input the word: ")
    if word == "":
        break
    print(dictionary.meaning(word))


# Si creo un diccionario puedo imprimir varios.
# dictionary = PyDictionary("eyes", "indentation", "head")
# print(dictionary.getMeanings())
