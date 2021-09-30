#!/usr/bin/env python3

import socket, sys
import select

PORT = 50001
TIMER = 1
MAX_INTENTOS = 3

"""NOTA:
Los números de los comentarios (entre paréntesis) identifican distintos
ejercicios. Es necesario realizar los distintos ejercicios de uno en
uno, probando su correcto funcionamiento antes de pasar al siguiente.
"""

if len( sys.argv ) != 2:
	print( "Uso: {} <servidor>".format( sys.argv[0] ) )
	exit( 1 )

"""A COMPLETAR POR EL ALUMNO:
(1) Usar la función gethostbyname para obtener la dirección IP del servidor y mostrarla en pantalla.
"""

HOST=socket.gethostbyname(sys.argv[1])
print("La IP del servidor que has introducido es: " + HOST)
dir_serv = (HOST, PORT)



s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
s.connect(dir_serv)

print( "Introduce el mensaje que quieres enviar (mensaje vacío para terminar):" )
while True:
	mensaje = input()
	if not mensaje:
		break
	"""A COMPLETAR POR EL ALUMNO:
	(2) Puesto que el socket es "conectado", sustituir 'sendto' por la función 'send'.
	(3) Usar la funcion 'select' para esperar el "eco" del mensaje
	    'TIMER' segundos como máximo. Si no se recibe, retransmitirlo.
	    Añadir un nuevo bucle para poder hacer varias retransmisiones.
	    Avisar al usuario por cada retransmisión realizada.
	(4) Controlar el numero máximo de transmisiones de un mensaje dado.
	    Avisar al usuario cuando se dé este hecho y terminar la ejecución.
	"""
	s.send( mensaje.encode())
	n=0
	while MAX_INTENTOS:
		rready,_,_ = select.select([s],[],[],TIMER)
		MAX_INTENTOS-=1

		if rready:
			buf = s.recv( 1024 )
			print( buf.decode() )
			break
		else:
			print("Imposible conectar con el servidor")
		


s.close()
