#  rattube.py
#  
#  Copyright 2020 Sam Sepiol <sam@debian>
#  


from pytube import YouTube
import time
from os import system,name
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format



class RatTube:

	def limpiar_Pantalla(self):
		if name=="nt":
			_=system('cls')	
		else:
			_=system('clear')
			
		''' Con este método comprobamos si la plataforma es NT (Windows) o si es Linux.
								
			Según el retorno boleano que se obtenga del método, ejecuta la instrucción usada en dicha
			plataforma para limpiar la consola'''	
			


	def mostrar_Banner(self):
		cprint(figlet_format('RatTube',font='banner3'),'yellow', 'on_blue', attrs=['bold'])
		
		
		'''Imprime el banner que se muestra en pantalla.
		
		el método cprint recibe parámetros texto,color del texto y fondo que tendrá el texto,
		attrs hace referencia a la fuente que sería en negrita
		el texto que recibe el método cprint es lo que se obtiene de
		formatearlo con el método figlet_format que lo convierte en ascii art y nos permite
		elegir fuentes que contiene la biblioteca pyfiglet'''
	
	def limpiar_Mostrar_Banner(self):
		self.limpiar_Pantalla()
		self.mostrar_Banner()
		
		'''Este método limpia la pantalla y muestra el banner.
		Se usa llamando los dos métodos juntos porque en la mayoría de los
		llamados se necesita que el banner siga ejecutándose manteniendo la pantalla
		limpia para dar enfoque a la tarea de descarga'''	

	
	def confirmar_Descargar(self):
			
			#self.confirmarDescargar()		
			url = input('\n\nIngresa la URL del video: ')
			ruta = input('\nEn qué ruta de tu equipo guardarás el archivo (si no pones una ruta, se guardará en el directorio del script)? ')
			video = YouTube(url) 
			print("\n",video.title) 
			stream = video.streams.first()
			stream.download(ruta)
			print('El video ha sido descargado en ', ruta) 
			tecla=input("\nPresione cualquier tecla para terminar")
			time.sleep(3)
			print("\n\nAdiós")
			
			'''Este método hace uso de la biblioteca pytube,de la clase Youtube y sus métodos.
			
			Permite realizar la descarga del video, pideo una url y la ruta de guardado
			por defecto se guarda en la carpeta donde esté el script'''
			
			
			
	def descargar(self):
		self.limpiar_Mostrar_Banner()
		print("""\n\n1. Ingresar URL del video
2. Volver""")
		opcion=input("\nElija una opción: ")
		
		if opcion=="1":
			self.confirmar_Descargar()
		else:
			self.limpiar_Mostrar_Banner()
			self.mostrar_Menu(self.descargar,self.salir)	
			
		'''Este método es para confirmar que si deseamos introducir la url del video.
		
		Si no nos hemos equivocado, confirmaremos que pondremos la url, en caso que no
		podremos dar en volver, ejecutando el método limpiar_Mostrar_Banner
		y llamando al menú inicial nuevamente'''
		
	def salir(self):
		self.limpiar_Pantalla()
		sys.exit()
		
	'''Si elegimos salir en el menu, se ejecuta este método.
	
	Nos permite terminar la ejecución del script sin interrumpir con el teclado'''	
		


	def mostrar_Menu(self,descargar,salir):
		print("""\n1. Descargar video de Youtube 
2. Salir""")
		choice=input("\nElija un opción: ")	
		opciones={"1":self.descargar,"2":self.salir}

		if choice=="1":
			eleccion=opciones[choice]()
			
			
		while choice not in opciones:
			print("\nNo se reconoce la opción")
			time.sleep(5)
			self.limpiar_Mostrar_Banner()
			self.mostrar_Menu(self.descargar,self.salir)
			
		else:
			eleccion=opciones[choice]()		
			
	'''Muestra el menú inicial.
	
	Llama desde aquí a los métodos necesarios para ejecutar las acciones
	de descarga o de salida del script'''			
		
		
rata=RatTube()
rata.limpiar_Pantalla()
rata.mostrar_Banner()
rata.mostrar_Menu(rata.descargar,rata.salir)
