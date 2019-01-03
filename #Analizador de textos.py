#Analizador de textos
#contador de letras
def contarletra(texto, letra):
	contador=0
	for l in texto:
		if l == letra:
			contador += 1
	return contador


while True:
	archivo=input("Introduce el nombre de el archivo: ")
	try:
		with open(archivo) as a:
			texto=a.read()
			print(texto)
			break
	except FileNotFoundError:
			print("******archivo no encontrado, prueba con la dirección completa del archivo******")
#a mejorar localización de archivo con mejora de skill propias.

#Aqui el usuario introduce una letra a contar en el texto
while True:
	caracter=str(input("introduce una letra y la contaré por tí en el texto: "))
	if caracter in texto:
		print("==========")
		print(contarletra(texto, caracter))
		print("==========================================================")
		print("para terminar el programa introduce: hasta la vista, baby ")
		print("==========================================================")
	elif caracter== "hasta la vista, baby":
		print("**********SAYONARA, BABY**********")
		break
