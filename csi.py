#!/usr/bin/env python
# -*- coding: utf-8 -*-

barva_las = ["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"] # Črna, Rjava, Korenček
oblika_obraza = ["GCCACGG", "ACCACAA", "AGGCCTCA"]      # Kvadraten, Okrogel, Ovalen
barva_oci = ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]  # Modra, Zelena, Rjava
spol = ["TGCAGGAACTTC", "TGAAGGACCTTC"]                 #Moški, Ženska
rasa = ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]          #Belec, Črnec, Azijec

ziga = [ spol[0], rasa[0], barva_las[2], barva_oci[2], oblika_obraza[1]]
matej = [ spol[0], rasa[0], barva_las[0], barva_oci[0], oblika_obraza[2]]
miha = [ spol[0], rasa[0], barva_las[1], barva_oci[1], oblika_obraza[0]]

dna = open("dna.txt", "r").read()

if (dna.find(ziga[0]) != -1 and dna.find(ziga[1]) != -1 and dna.find(ziga[2]) != -1 and dna.find(ziga[3]) != -1):
    print ("Bil je Žiga!")
elif (dna.find(matej[0]) != -1 and dna.find(matej[1]) != -1 and dna.find(matej[2]) != -1 and dna.find(matej[3]) != -1):
    print ("Bil je Matej!")
elif (dna.find(miha[0]) != -1 and dna.find(miha[1]) != -1 and dna.find(miha[2]) != -1 and dna.find(miha[3]) != -1):
    print ("Bil je Miha!")
else :
    print ("Krivca ni med osumljenci..")
