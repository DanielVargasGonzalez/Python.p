#juego rpg
from random import randint
class personaje:
	def __init__(self, nombre, estado, salud, salud_max):
		self.nombre = nombre
		self.estado = estado
		self.salud = salud
		self.salud_max = salud_max
		
	#funcion danio con random
	def hacer_danio_enemigo(self, x):
		danio= min(max(randint(0, self.salud) - randint(0, x.salud), 0), x.salud)
		x.salud-= danio
		if danio == 0:
			print("***Grimoriano evadio el ataque de el goblin***")
		else:
			print("***un ataque de el goblin alcanzó a Grimoriano!!***")
			return x.salud <= 0	
	
	def hacer_danio(self, x):
		danio= min(max(randint(0, self.salud) - randint(0, x.salud), 0), x.salud)
		x.salud-= danio
		if danio == 0:
			print("***El goblin evadio un ataque de Grimoriano***")
		else:
			print("***un ataque de Grimoriano alcanzó a el goblin!!***")
			return x.salud <= 0

#clase enemigo 
class enemigo (personaje):
	def __init__(self):
		personaje.__init__(self, "goblin", "normal", 3, 3)
		#self.nombre= "trasgo"
		#self.salud= randint(1, jugador.salud)
		
#jugador

class jugador(personaje):
	def __init__(self):
		personaje.__init__(self, "Grimoriano", "normal", 4, 4 )
	##	self.nombre = "Grimoriano"
	##	self.estado = "normal"
	##	self.salud = 10
	#	self.salud_max = 10

#acciones de jugador
	def salir(self):
		print("Grimoriano trata de salir, pero es un paquete en orientación, asi que se pierde, y muere de hambre \n **R.I.P**")
		self.salud = 0

	def ayuda(self):
		print(Commands.keys())

	def estado(self):
		print ("%s - salud: %d/%d" % (self.nombre, self.salud, self.salud_max))

	def cansancio(self):
		print("%s siente cansancio." % self.nombre)
		self.salud = self.salud - 1
		print ("%s - salud: %d/%d" % (self.nombre, self.salud, self.salud_max))	

	def explorar(self):
		if self.estado != "normal":
			print ("%s está ocupado" % self.nombre)
			self.enemigo_ataques()
		else:
			print ("%s explora los tuneles y descubre una nueva camara subterranea" % self.nombre)
			if randint(0, 1):
				print("%s encuentra un enemigo!" % self.nombre)
				self.estado = "lucha"

			else:
				if randint(0,1):
					self.cansancio()
	
	def huir(self):
		if self.estado != "lucha":
			print("el miedo se apodera de Grimoriano, intentas huir de la cueva, pero eres tan parguelas que no encuentras el camino de vuelta.")
			self.cansancio()
		else:
			if randint(0,1):
				print("%s huye cual perra del inframundo" % self.nombre)
				self.enemigo = None
				self.estado = "normal"
			else:
				print("Grimoriano intenta escapar, pero el goblin pueder ver sus intenciones, lanza un ataque y...")
				self.enemigo_ataques()
	
	def atacar(self):
		if self.estado != "lucha":
			print("%s golpea el aire, *no se que pretendes*" % self.nombre)
			self.cansancio()
		else:
			if jugador.hacer_danio(self,enemigo()):
				print("Grimoriano mata al goblin")
				self.enemigo = None
				self.estado = "normal"
				if randint(0, self.salud) < 10:
					self.salud += 1
					self.salud_max += 1
					print("Grimoriano se siente más fuerte")
			else:
				self.enemigo_ataques()

	def enemigo_ataques(self):
		if enemigo.hacer_danio_enemigo(self, w):
			print ("el goblin mata y viola a Grimoriano, \n ***HAS PERDIDO***!!!!") 

	def descanso(self):
		if self.estado != "normal":
			print ("Grimoriano no puede descansar ahora!") 
			self.enemigo_ataques()

		else:
			print("Grimoriano descansa") 

			if randint(0 , 1):
				print("Grimoriano se desperto de golpe por el ruido de un goblin, este está a punto de lanzar un ataque!")
				self.estado = "lucha"
				self.enemigo_ataques()
			else:
				if self.salud < self.salud_max:
					self.salud = self.salud + 1
				else:
					print ("Grimoriano ha dormido demasiado."); self.salud -= 1

#comandos
Commands = {
	"salir" : jugador.salir,
	"ayuda" : jugador.ayuda,
	"estado" : jugador.estado,
	"descanso" : jugador.descanso,
	"explorar" : jugador.explorar,
	"huir" : jugador.huir,
	"atacar" : jugador.atacar,
	}

#apertura de juego
w= jugador()
print ("Un dia cualquiera, en una ciudad cualquiera, habia un informático llamado Grimoriano, \n el cual estaba haciendo un codido de un juego de rol llamado...")
p = input("***pulsa enter para continuar***")
print ("**Grimoriano & Mazmorras** \n Por culpa de el cambio climático un portal interdimensional se abrió, absorbiendo a nuestro protagonista \n y llevandolo a un mundo de fantasía plagado de criaturas mágicas. \n Al observarse a sí mismo se dió cuenta de que se habia convertido \n en un AVENTURERO de armadura y espada. \n ante él habia una mazmorra, y como buen AVENTURERO entró en ella")
print ("***escribre ayuda para obtener una lista de acciones***")

#Ciclo de juego
while (w.salud > 0):
	line = input("> ")
	args = line.split()
	if len(args) > 0:
		commandsFound = False
		for c in Commands.keys():
			if args[0] == c[:len(args[0])]:
				Commands[c](w)
				commandsFound == True
				break
		if commandsFound:
			print("acción no válida.")