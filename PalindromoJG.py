word = input("Ingrese palabra a comprobar: ")
wordc = ''.join(filter(str.isalpha, word))
if wordc.lower() == wordc[::-1].lower():
    print("Sí es un palíndromo")
else:
    print("No es un palíndromo")
