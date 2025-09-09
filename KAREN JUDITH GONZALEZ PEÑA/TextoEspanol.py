import re 
#with open('espanol.txt', 'r', encoding='latin-1') as f:
   # texto_espanol = f.read()

texto_espanol =" En el año 2025, 24 diseñadores crean juntos. ¡Hola! ¿Te gusta el diseño? El cielo creativo, las estrellas (★) brillan. 20 niños dibujan, 19.50 horas de inspiración. Lista: lápiz, papel, regla. El costo es $95.20. ¿Sabías que el código #3344 es especial? La vida es arte, @todos participan. El tiempo pasa, 21 días de creatividad. ¡Diseña! El número especial es 1414. ¿Qué harías con 60.90 pesos? La respuesta está en la lista: dibujar, crear, innovar. ¡Diseña tu mundo! 100 palabras, 21 enteros, 3 decimales, 2 listas."
# se crean las variables correspondientes para cada tipo de busqueda y se les asigna el comando para encontar los respectivos tipos de datos 
enteros = r"\b-?\d+\b"
flotantes= r"\b-?\d+\.\d+\b"
booleanos = r"\b(True|False)\b"
strings = r'"(.*?)"'
listas =  r"(?i)lista:\s*([^.\n]+)"
palabras =  r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+\b"
#palabras = r"\b[\wáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙñÑüÜ]+\b"

buscar_enteros = re.findall(enteros,texto_espanol) 
buscar_flotantes = re.findall( flotantes,texto_espanol)
buscar_booleanos = re.findall( booleanos,texto_espanol)
buscar_strings= re.findall( strings,texto_espanol)
buscar_listas_num = re.findall(listas,texto_espanol)
buscar_palabras = re.findall(palabras,texto_espanol)

# se imprimen  los resultados de cada busqueda y tambien se imprime la cantidad total de elmentos encontrados para cada tipo de dato
print(" LOS RESULTADOS SON :")
print("se encontraron los enteros   :",buscar_enteros,"    una cantidad total de :", len(buscar_enteros),  " numeros enteros en el texto ")
print("se encontraron los flotantes :",buscar_flotantes,"  una cantidad total de :", len(buscar_flotantes),"numeros flotantes en el texto")
print("se encontraron los booleanos :",buscar_booleanos,"  una cantidad total de :", len(buscar_booleanos),"valores booleanos en el texto")
print("se encontraron los strings   :",buscar_strings,"    una cantidad total de :", len(buscar_strings),  " strings en el texto")
print(" se encontraron las listas   :",buscar_listas_num," una cantidad total de :", len(buscar_listas_num),"listas en el texto")
print(" se encontraron las palabras :",buscar_palabras ,"  una cantidad total de :", len(buscar_palabras),"palbras en el texto")