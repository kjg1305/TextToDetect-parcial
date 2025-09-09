import re 
#with open('italiano.txt', 'r', encoding='latin-1') as f:
   # texto_espanol = f.read()

texto_espanol =" Ciao! Nel 2025, 23 designer creano insieme. Lista: matita, carta, righello. Il prezzo è €90,80. Le stelle (★) brillano sopra il foglio. 17 gatti disegnano, 16 cani creano. Il codice #7788 è speciale. 20 giorni di creatività, 16 di riposo. @tutti creano. Il numero magico è 1434. Cosa faresti con 57,90€? La risposta è nella lista: disegnare, creare, innovare. Immagina il tuo mondo! 100 parole, 20 interi, 3 decimales, 2 listas."
# se crean las variables correspondientes para cada tipo de busqueda y se les asigna el comando para encontar los respectivos tipos de datos 
enteros = r"\b-?\d+\b"
flotantes= r"\b-?\d+\,\d+\b"
booleanos = r"\b(True|False)\b"
strings = r'"(.*?)"'
listas =  r"(?i)lista:\s*([^.\n]+)"
palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙñÑüÜ]+\b"

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