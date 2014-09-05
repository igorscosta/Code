#!/usr/bin/python


#### Ferramenta para levantar dados de Sistemas Linux #######
#
# Autor: Frederico Gomes	fredd.demolay@gmail.com
#
#Versao: 0.1
########################## Programa ########################

import os

def dadosCPU():
	cmd = os.system("iostat -c")

def numCPUs():
	cmd = os.system("mpstat -P ALL")

def visaoGeral():
	print "Para sair aperte 'q'"
	timer = os.system("sleep 2")
	cmd = os.system("top")

def memLivre():
	cmd = os.system("free")


def mostraProcesso():
	print "<enter> para passar, <q> para sair!"
	timer = os.system("sleep 2")
	cmd = os.system("ps -A | more")


def upTime():
	print "Veja desde quando o sistema esta rodando, funcionando, considerando inclusive quaisquer reboots que tenham sido executados."
	cmd = os.system("uptime")

def usuarioLogado():
	print "usuario(s) logado(s):"
	cmd = os.system("w")

def arvoreProcesso():
	cmd = os.system("pstree")

def Menu():
	menu = raw_input("Levantar dados: s/n -- CTRL^C para SAIR: ")
	if menu == 's':	
		print "Escolha uma opacao"
	
		print "  dados da CPU - 1"
		print "  numero de CPUs - 2"
		print "  visao geral do sistema - 3"
		print "  memoria livre - 4"
		print "  processos - 5"
		print "  dados do sistema - 6"
		print "  usuarios logados - 7"
		print "  mostrar arvore de processos - 8"
		print "  SAIR - 0"

		opcao = int(raw_input("Entrada:"))

		if opcao == 1:
			dadosCPU()
		elif opcao == 2:
			numCPUs()
		elif opcao == 3:
			visaoGeral()
		elif opcao == 4:
			memLivre()
		elif opcao == 5:
			mostraProcesso()
		elif opcao == 6:
			upTime()
		elif opcao == 7:
			usuarioLogado()
		elif opcao == 8:
			arvoreProcesso()		
		else:
			print "saindo..."
########################## Principal ########################

if __name__ == "__main__":
	
	while 1:
	
		Menu()
	
	
