#calculadora, proyecto 1
#Saludo inicial
def saludin():
	saludo="Bienvenido a la calculadora grimoriana"
	print(saludo)
	
def decorar(func):
	def envoltorio():
		print("="*38)
		func()
		print("="*38)
	return envoltorio
saludeco=decorar(saludin)
saludeco()

#pasamos al menu
def menu():
	print("para sumar introduce: 1")
	print("para restar introduce: 2")
	print("para multiplicar introduce: 3")
	print("para dividir introduce: 4")
	print("para elevar introduce: 5")
	print("para una raiz introduce: 6")
	print("para el entero de una división introduce: 7")
	print("para el resto de una división introduce: 8")
	print("para salir introduce: 9")
	#ahora pedimos una opción y validamos.
def elegir():
	intentos=0
	while intentos<=5:
		opcion=input("introduce una opción: ")
		try:
			opcion=int(opcion)
			if opcion<=0:
				print("*****Escriba uno mayor a 0: ")
			elif opcion>9:
				print("*****Escriba uno menor a 10: ")
			else:
				break 
		except ValueError:
			intentos+=1
			print("*********opción no valida, prueba otra vez")
			if intentos>=6:
				raise ValueError("A cerrar el programa, esto te pasa por meter letras en vez de numeros ¬¬")
	return opcion
def menuelec():
	menu()
	elegir()

import msvcrt
while True:
	menu()
	eleccion=elegir()
	if eleccion==1:
		def suma():
			totalsuma=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("*****introducción no valida, introduce un número")
			while True:
				numero2=(input("introduce el segundo número: "))
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("*****introducción no valida, introduce un número")
			totalsuma=numero1+numero2
			pego="******el total es: "
			pegototal=pego+str(totalsuma)+"******"
			print("="*38)
			print(pegototal)
		decosuma=decorar(suma)
		decosuma()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==2:
		def resta():
			totalresta=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("*****introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("*****introducción no valida, introduce un número")
			totalresta=numero1-numero2
			pego="******el total es: "
			pegototal=pego+str(totalresta)+"******"
			print("="*38)
			print(pegototal)
		decoresta=decorar(resta)
		decoresta()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==3:
		def multiplicacion():
			totalmultiplicacion=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("*****introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("*****introducción no valida, introduce un número")
			totalmultiplicacion=numero1*numero2
			pego="******el total es: "
			pegototal=pego+str(totalmultiplicacion)+"******"
			print("="*38)
			print(pegototal)
		decomultiplicacion=decorar(multiplicacion)
		decomultiplicacion()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==4:
		def division():
			totaldivision=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			totaldivision=numero1/numero2
			pego="******el total es: "
			pegototal=pego+str(totaldivision)+"******"
			print("="*38)
			print(pegototal)
		decodivision=decorar(division)
		decodivision()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==5:
		def elevar():
			totalelevar=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			totalelevar=numero1**numero2
			pego="******el total es: "
			pegototal=pego+str(totalelevar)+"******"
			print("="*38)
			print(pegototal)
		decoelevar=decorar(elevar)
		decoelevar()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==6:
		def raiz():
			totalraiz=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			totalraiz=numero1**1/numero2
			pego="******el total es: "
			pegototal=pego+str(totalraiz)+"******"
			print("="*38)
			print(pegototal)
		decoraiz=decorar(raiz)
		decoraiz()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==7:
		def entero():
			totaldivision=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			totalentero=int(numero1//numero2)
			pego="******el total es: "
			pegototal=pego+str(totalentero)+"******"
			print("="*38)
			print(pegototal)
		decoentero=decorar(entero)
		decoentero()
		print("****** presione enter para volver al menu******")
		input("")

	elif eleccion==8:
		def restodivi():
			totalrestodivi=0
			while True:
				numero1=input("introduce el primer número: ")
				try:
					numero1=float(numero1)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			while True:
				numero2=input("introduce el segundo número: ")
				try:
					numero2=float(numero2)
					break
				except ValueError:
					print("****** introducción no valida, introduce un número")
			totalrestodivi=numero1 % numero2
			pego="******el total es: "
			pegototal=pego+str(totalrestodivi)+"******"
			print("="*38)
			print(pegototal)
		decorestodivi=decorar(restodivi)
		decorestodivi()
		print("****** presione enter para volver al menu******")
		input("")

	else:
		print("***Adios, vuelve pronto***")
		break