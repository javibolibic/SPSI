#! /usr/bin/python
# -*- coding: utf-8 -*-

from fractions import gcd

"""
Run the Kasiski test on a ciphertext string.

The Kasiski test reports the distance between repeated
strings in the ciphertext.
"""

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


lista_ocurrencias = []

def findsubs(text, l):
	"""
	Find all repeated substrings of length 'l' in 'text'
	"""
	for i in range(len(text)-l):
		subcadena = text[i:i+l]
		found = text[i+l:].find(subcadena)
		if found != -1:
			# if the match can be extended in either direction, don't
			# report it
			f = found+i+l
			if i>0 and text[i-1:i+l] == text[f-1:f+l]:
				continue
			if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
				continue            
			print "%-10s %3d " % (subcadena, found+l)
			a = found+l
			lista_ocurrencias.append(a)
			# print lista_ocurrencias[len(lista_ocurrencias)-1]
			#print "%-10s %3d %s" % (subcadena, found+l, str(factor(found+l)))
			   

def ktest(text):
	"""
	Strip all characters that are not in the cipher alphabet.

	Report all substrings from longest to shortest.  The longest
	possible substring is half the ciphertext length.  Substrings
	shorter than 5 are not reported.
	"""
	ctext = ""
	for c in text:
		c = c.upper()
		if c in alphabet:
			ctext += c          

	"""
	el tamaño máximo de una cadena que se puede repetir en el texto tiene 
	de tamaño como máximo la longitud del texto / 2. Empieza desde esa longitud hacia abajo.
	"""
	for l in range(len(text)/2,2,-1):
	    findsubs (ctext, l)    
	mcd = reduce(gcd,lista_ocurrencias)
	print "MCD = " + str(mcd)
	"""
	dividir el texto en cadenas de tamaño MCD
	""" 
	print "tamaño del texto = " + str(len(ctext))
	tam_subcadena = int(len(ctext)/mcd)
	print "n_iter = " + str(tam_subcadena)
	i=0
	subcadena=[100000]
	for l in range(0,len(ctext),tam_subcadena):
		if l + tam_subcadena > len(ctext):
			sobrante = l + tam_subcadena - len(ctext)
			len_intervalo = l + tam_subcadena - sobrante
		else:
			len_intervalo = l + tam_subcadena
		subcadena[i] = ctext[l:len_intervalo]
		i+=1
		print "subcadena = " + str(tam_subcadena)

if __name__ == "__main__":
    def main():
        while True:
            text = raw_input ("Give me ciphered text? \n")
            if len(text) == 0:
                break
            ktest(text)
            print text
    main()







# *************************************CADENA DE EJEMPLO AQUÍ*************************************
# PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU