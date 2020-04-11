
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
						
	
	def mostrarBanner(self):
		cprint(figlet_format('RatTube',font='banner3'),'yellow', 'on_blue', attrs=['bold'])
		
		
		'''Imprime el banner que se muestra en pantalla.
		
		el método cprint recibe parámetros texto,color del texto y fondo que tendrá el texto,
		attrs hace referencia a la fuente que sería en negrita
		el texto que recibe el método cprint es lo que se obtiene de
		formatearlo con el método figlet_format que lo convierte en ascii art y nos permite
		elegir fuentes que contiene la biblioteca pyfiglet'''
	
	def limpiarMostrarBanner(self):
		self.limpiar_Pantalla()
		self.mostrarBanner()
		
		'''Este método limpia la pantalla y muestra el banner.
		Se usa llamando los dos métodos juntos porque en la mayoría de los
		llamados se necesita que el banner siga ejecutándose manteniendo la pantalla
		limpia para dar enfoque a la tarea de descarga'''	

	
	def confirmarDescargar(self):
			
			#self.confirmarDescargar()		
			url = input('\n\nIngresa a URL del video: ') #Ingresar url del video a descargar
			ruta = input('\nEn qué ruta de tu equipo guardarás el archivo? ') #ingresar la direccion donde el video se guardara
			video = YouTube(url) #Obtener el video de Youtube 
			print("\n",video.title) #Mostrar el titulo del video que se descargara
			stream = video.streams.first()
			#file_size=stream.filesize
			stream.download(ruta) #Descargar video en la carpeta indicada
			print('El video ha sido descargado en ', ruta) 
			tecla=input("\nPresione cualquier tecla para terminar")
			time.sleep(3)
			print("\n\nAdiós")
			
			
			
			
	def descargar(self):
		self.limpiarMostrarBanner()
		print("""\n\n1. Ingresar URL del video
2. Volver""")
		opcion=input("\nElija una opción: ")
		
		if opcion=="1":
			self.confirmarDescargar()
			
		
		else:
			self.limpiarMostrarBanner()
			self.mostrar_Menu(self.descargar,self.salir)	
		
	
	def salir(self):
		self.limpiar_Pantalla()
		sys.exit()
		
		

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
			self.limpiarMostrarBanner()
			self.mostrar_Menu(self.descargar,self.salir)
			
		else:
			eleccion=opciones[choice]()		
				
		
		
rata=RatTube()
rata.limpiar_Pantalla()
rata.mostrarBanner()
rata.mostrar_Menu(rata.descargar,rata.salir)
