lista=["a","b","c","d","e","f","g","h"]
for i in lista:
    posision =lista.index(i)
    print(f" letra  {i} en la pocicion {posision}" )

    
lista_nombres =["Mairio","Juan","Carla","Mishel"]    
for nombre in lista_nombres:
    if nombre.startswith("l"):
        print(nombre)

palabra="python"

for letra in palabra:
    print(letra)

alumnos_clase = ["Mario", "Juan", "Carlos", "Mishelle", "Isabela", "Andres", 
 "Daniela"]

for i in alumnos_clase:
     print(f"hola {i}")
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for i in lista_numeros:
     suma_numeros =suma_numeros +i 
print(f"la suma es de {suma_numeros}")    

lista_numeros2 = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares =0
suma_impares =0
for i in lista_numeros2:
    if i % 2 == 0:
        suma_pares=suma_pares+i
    elif i%2==1:
        suma_impares=suma_impares+i   
print(f"suma de numero pares = {suma_pares}  la suma de los numero impares = {suma_impares}")  
