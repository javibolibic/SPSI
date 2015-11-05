#! /usr/bin/python
# -*- coding: utf-8 -*-
#######
from fractions import gcd

"""
Run the Kasiski test on a ciphertext string.

The Kasiski test reports the distance between repeated
strings in the ciphertext.
"""

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

#    from crypt import *
lista = []
def findsubs(text, l):
    """
    Find all repeated substrings of length 'l' in 'text'
    """
    for i in range(len(text)-l):
        target = text[i:i+l]
        found = text[i+l:].find(target)
        
        if found != -1:
            # if the match can be extended in either direction, don't
            # report it
            f = found+i+l
            if i>0 and text[i-1:i+l] == text[f-1:f+l]:
                continue
            if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
                continue            
            # print "%-10s %3d " % (target, found+l)
            print target,'   ', found+l
            lista.append(found+l)
            #print "%-10s %3d %s" % (target, found+l, str(factor(found+l)))
	print 'la longitud de la lista es: ', len(lista)
	for l in range(len(lista)):
		print lista[l]
	# return lista
   

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
	
    for l in range(len(text)/2,2,-1):
        findsubs(ctext, l)
        
    # print 'IMPRIMIENDO LISTA:'
    # for i in range(len(a)):
    #     print a[i]

        
def mcd(lista):
	a = [4,10,16,14]  #or else simply take input from user
	#a = map(int,raw_input().split())   #this line assumes list to be passed in with numbers seperated by white spaces
	print reduce(gcd,lista)


if __name__ == "__main__":
    def main():
        while True:
            text = raw_input ("Give me ciphered text? \n")
            if len(text) == 0:
                break
            ktest(text)
            # print text
    main()
