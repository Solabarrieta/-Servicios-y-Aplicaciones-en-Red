#!/usr/bin/env python3

import socket

PORT = 50002

"""A COMPLETAR POR EL ALUMNO:
Crear un socket, asignarle su dirección y
convertirlo en socket de escucha.
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 51001))

s.listen(5)

while True:
	"""A COMPLETAR POR EL ALUMNO:
	Aceptar peticion de conexion.
	Mientras el cliente no cierre la conexion,
	recibir un mensaje y responder con el mismo.
	Cerrar conexión.
	"""
	
	dialog,_ = s.accept()

	while True:	
		mensaje = dialog.recv(1024)

		if not mensaje:
			dialog.close()
			break
		dialog.sendall(mensaje)


"""A COMPLETAR POR EL ALUMNO:
Cerrar socket de escucha.
"""
s.close()


