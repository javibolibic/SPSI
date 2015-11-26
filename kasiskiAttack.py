#! /usr/bin/python
# -*- coding: utf-8 -*-

from fractions import gcd
import sys
import collections


# alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"
spanish = 0.0775


# Desencripta el texto plano a cifrado vigenère
def decrypt(cipher, key):
	key_index = 0
	plain = ''
	for i in cipher:
		plain += chr((ord(i)-ord(key[key_index])-2*65) %26 +65)
		if key_index < len(key) - 1:
			key_index += 1
		else:
			key_index = 0
	return plain

"""
busca todas las subcadenas de longitud 'l' en 'text'
modifica la variable global lista_ocurrencias, añadiendo la distancia entre dichas repeticiones.
"""
def findsubs(text, l, lista_ocurrencias):
	for i in range(len(text)-l):
		subcadena = text[i:i+l]
		found = text[i+l:].find(subcadena)
		if found != -1:
			f = found+i+l
			if i>0 and text[i-1:i+l] == text[f-1:f+l]:
				continue
			if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
				continue            
			print "%-10s %3d " % (subcadena, found+l)
			a = found+l
			lista_ocurrencias.append(a)    
	return lista_ocurrencias
"""
excluye caracteres de text que no estan en el alfabeto alphabet
"""            
def filter(text):
	ctext = ""
	for c in text:
		c = c.upper()
		if c in alphabet:
			ctext += c
	return ctext

def imprime(cadena):
	sys.stdout.write("***** ")
	for i in range(len(cadena)):
		sys.stdout.write(cadena[i])
	sys.stdout.write(" *****")
	print""


def indexofCoincidence(cadena, i):
	N = len(cadena[i])
	freqs = collections.Counter( cadena[i] )
	freqsum = 0.0

	for letter in alphabet:
		freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

	IC = freqsum / (N*(N-1))
	return IC

def splitText(ctext, mcd):
	cadena=[[] for x in range(mcd)]  
	for i in range(0, (len(ctext)/mcd)):
		j=0
		if i == 0:
			for j in range(0,mcd):
				cadena[j].append(ctext[j])
		else:
			for j in range(0,mcd):
				if i*mcd+j<len(ctext):
					cadena[j].append(ctext[i*mcd+j])
	return cadena

def ktest(text):
	lista_ocurrencias = []
	ctext = filter(text)        

	"""
	el tamaño máximo de una cadena que se puede repetir en el texto tiene 
	de tamaño como máximo la longitud del texto / 2. Empieza desde esa longitud hacia abajo.
	"""
	for l in range(len(text)/2,2,-1):
		findsubs (ctext, l, lista_ocurrencias)
	if len(lista_ocurrencias)==0:
		# print "asasdfasdfasdf"
		sys.exit("No se han encontrado cadenas repetidas")
	
	mcd = reduce(gcd,lista_ocurrencias) #cálculo del máximo común divisor
	print "Posible longitud de la clave = " + str(mcd)
	if mcd ==1:
		print "El programa no es concluyente. De la distancia entre subcadenas repetidas no se puede extraer un tamaño de clave"
		# sys.exit(0)
	print ""

	cadena = splitText(ctext, mcd)
					
	for i in range(len(cadena)):
		sys.stdout.write("cadena[" + str(i) + "]== ")
		for j in range(len(cadena[i])):
			sys.stdout.write(cadena[i][j])
		print ""
	print ""

	"""
	contar las letras que más se repiten en cada una de las cadenas
	""" 
	ocurrencias=0
	clave=[]

	vocurrencias=[[] for x in range(mcd)] #ocurrencias de cada caracter c en cada subcadena 
	for i in range(0, mcd):
		for c in alphabet:
			ocurrencias = cadena[i].count(c);
			vocurrencias[i].append(ocurrencias)
		max1=0
		max2=0
		max3=0
		letra1=''
		letra2=''
		letra3=''
		maxocurrencias1=0
		maxocurrencias2=0
		print "alfabeto: " + str(alphabet)
		print "vocurrencias: " + str(vocurrencias[i])
		for k in range(0, len(alphabet)):
			cantidad = vocurrencias[i][k%len(alphabet)]
			cantidad +=vocurrencias[i][(k+4)%len(alphabet)]
			cantidad +=vocurrencias[i][(k+15)%len(alphabet)]
			if cantidad > max1:
				max3=max2
				max2=max1
				max1=cantidad
				letra3=letra2
				letra2=letra1
				letra1=alphabet[k]
			elif cantidad > max2:
				max3=max2
				max2=cantidad
				letra3=letra2
				letra2=alphabet[k]
			elif cantidad > max3:
				max3=cantidad
				letra3=alphabet[k]
		print "Primera letra más probable: " + letra1
		print "Segunda letra más probable: " + letra2
		print "Tercera letra más probable: " + letra3

		"""
		Cálculo del íncide de coincidencia
		"""
		IC = indexofCoincidence(cadena, i)

		print "Indice de coincidencia de cadena[" + str(i) + "] %.3f" % IC, "({})".format( IC )
		if IC < spanish:
			print "(NO FIABLE)\n"
		else:
			print"(FIABLE)\n"
		clave.append(letra1)
	
	"""
	imprimir las claves
	""" 
	sys.stdout.write("POSIBLE CLAVE\t")
	imprime(clave)
	clavestring = ''.join(clave)
	plano = decrypt(ctext, clavestring)
	print "Posible texto plano: " + str(plano)
	

if __name__ == "__main__":
	def main():
		while True:
			text =raw_input ("Introducir el texto cifrado: \n")
			if len(text) == 0:
				break
			ktest(text)
	main()


# *************************************CADENA DE EJEMPLO AQUÍ*************************************
# PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU
# PPQCAXQV EKGYBNKM AZUYBNGB ALJONITS ZMJYIMVR AGVOHTVR AUCTKSGD DWUOXITL AZUVAVVR AZCVKBQP IWPOU


