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
    n_iter = int(len(ctext)/mcd)
    print "n_iter = " + str(n_iter)
    # HACER BUCLE Y PARTIR EL TEXTO EN SUBCADENAS

if __name__ == "__main__":
    def main():
        while True:
            text = raw_input ("Give me ciphered text? \n")
            if len(text) == 0:
                break
            ktest(text)
            print text
    main()











































# #! /usr/bin/python
# # -*- coding: utf-8 -*-
# #######
# from fractions import gcd

# """
# Run the Kasiski test on a ciphertext string.

# The Kasiski test reports the distance between repeated
# strings in the ciphertext.
# """

# alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# #    from crypt import *
# lista = []
# def findsubs(text, l):
#     """
#     Find all repeated substrings of length 'l' in 'text'
#     """
#     for i in range(len(text)-l):
#         target = text[i:i+l]
#         found = text[i+l:].find(target)
        
#         if found != -1:
#             # if the match can be extended in either direction, don't
#             # report it
#             f = found+i+l
#             if i>0 and text[i-1:i+l] == text[f-1:f+l]:
#                 continue
#             if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
#                 continue            
#             # print "%-10s %3d " % (target, found+l)
#             print target,'   ', found+l
#             lista.append(found+l)
#             #print "%-10s %3d %s" % (target, found+l, str(factor(found+l)))
   

# def ktest(text):
#     """
#     Strip all characters that are not in the cipher alphabet.
    
#     Report all substrings from longest to shortest.  The longest
#     possible substring is half the ciphertext length.  Substrings
#     shorter than 5 are not reported.
#     """
#     ctext = ""
#     for c in text:
#         c = c.upper()
#         if c in alphabet:
#             ctext += c
# 	#el tamaño máximo de una cadena que se puede repetir en el texto tiene de tamaño como máximo la longitud del texto / 2
#     #empieza desde esa longitud hacia abajo.
#     for l in range(len(text)/2,2,-1):
#         findsubs(ctext, l)
        
#     # print 'IMPRIMIENDO LISTA:'
#     # for i in range(len(a)):
#     #     print a[i]

        
# def mcd(lista):
# 	a = [4,10,16,14]  #or else simply take input from user
# 	#a = map(int,raw_input().split())   #this line assumes list to be passed in with numbers seperated by white spaces
# 	print reduce(gcd,lista)


# if __name__ == "__main__":
#     def main():
#         while True:
#             text = raw_input ("Give me ciphered text? \n")
#             if len(text) == 0:
#                 break
#             ktest(text)
#             # print text
#     main()
