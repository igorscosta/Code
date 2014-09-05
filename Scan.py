#!/bin/python

#scanner de portas em python
#Autor: Frederico Gomes
#Versao: 1.2

#importando modulos
import socket
import sys

HOST = raw_input("Entre com o ip:")  #definindo endereco de ip
PORT = 0  #definindo porta
#varrendo as portas
for PORT in range(65000):
	#criando o socket
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#conectando....
	res = tcp.connect_ex((HOST, PORT))
	#name = socket.gethostname()
	#caso seja diferente de zero, a porta esta fechada
	if res == 0:
		print "Porta: %d aberta" %PORT
		tcp.close()

#verifica o nome do host
name = socket.gethostname()
print "Nome do host: ", name
print "Varredura encerrada "
