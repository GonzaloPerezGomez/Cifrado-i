
def descifrar(msg):
	str(msg)
	frecuencias = {}
	dicc = ["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]
	
	for letra in msg:
		if letra.isalpha():
			frecuencias[letra] = frecuencias.get(letra, 0) + 1

	frecuencias = dict(sorted(frecuencias.items(), key=lambda item: item[1], reverse=True))
	print(frecuencias)


mensaje = input(f"Introduce el mensaje a cescifrar: ")
descifrar(mensaje)
	


