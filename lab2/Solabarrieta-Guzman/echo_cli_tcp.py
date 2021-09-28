#!/usr/bin/env python3

import socket, sys

PORT = 50002

# Comprueba que se ha pasado un argumento.
if len( sys.argv ) != 2:
	print( "Uso: {} <servidor>".format( sys.argv[0] ) )
	exit( 1 )

"""A COMPLETAR POR EL ALUMNO:
Crear un socket y enviar peticion de conexion al servidor.
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((sys.argv[1], 51001))


print( "Introduce el mensaje que quieres enviar (mensaje vacío para terminar):" )
while True:
	mensaje = input()
	if not mensaje:
		break
	"""A COMPLETAR POR EL ALUMNO:
	Enviar mensaje y recibir 'eco'.
	Mostrar en pantalla lo recibido.
	¡Cuidado! Recuerda que no hay garantías de recibir
	el mensaje completo en una única lectura.
	"""
	mensajeEncoded = mensaje.encode()
	s.sendall(mensajeEncoded)
	
	mensaje_eco = b""
	while True: 
		buf = s.recv(1024)
		mensaje_eco+=buf
		if mensaje_eco == mensajeEncoded:
			break
	
	print(mensaje_eco.decode())
s.close()
