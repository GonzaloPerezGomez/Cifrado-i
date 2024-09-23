
def descifrar(msg):
	str(msg)
	frecuencias = {}
	dicc = ["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]
	
	for letra in msg:
		if letra.isalpha():
			frecuencias[letra] = frecuencias.get(letra, 0) + 1

	frecuencias = dict(sorted(frecuencias.items(), key=lambda item: item[1], reverse=True))

	mapeo = {str : str}
	i = 0
	for letra in frecuencias:
		mapeo[letra] = dicc[i]
		i+=1

	desentriptado = []
	for letra in msg:
		if letra.isalpha():
			desentriptado.append(mapeo[letra])
		else:
			desentriptado.append(letra)

	return ''.join(desentriptado)


mensaje = input(f"Introduce el mensaje a cescifrar: ")
mensaje = descifrar(
	"""RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
	AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
	AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
	TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
	DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
	PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
	TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
	HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
	HKCZJOI OKEJSZCNHE"""
	)
print(mensaje)

finished = False

while not finished:
	print("¿Quieres cambiar algo? (Y/N)")
	if input() == "Y":
		prim = input(f"¿Que letra quieres cambiar?")
		sec = input(f"¿Por que letra la quieres cambiar?")
		mensaje = mensaje.replace(prim.lower(), sec.lower())
		print(mensaje)
	else:
		finished = True
	

	


