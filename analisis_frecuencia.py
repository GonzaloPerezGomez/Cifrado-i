
def descifrar(msg):
	str(msg)
	frecuencias = {}	
	
	for letra in msg:
		if letra.isalpha():
			if letra in frecuencias:
				frecuencias[letra] += 1
			else:
				frecuencias[letra] = 1

	print(frecuencias)


mensaje = input(f"Introduce el mensaje a cescifrar: ")
descifrar(mensaje)
	


