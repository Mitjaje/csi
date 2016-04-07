#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
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
'''

###############Resitev z uporabo dictionary########################


barva_las = {
    "crna":"CCAGCAATCGC",
    "rjava":"GCCAGTGCCG",
    "korencek":"TTAGCTATCGC"
}
oblika_obraza = {
    "kvadraten":"GCCACGG",
    "okrogel":"ACCACAA",
    "ovalen":"AGGCCTCA"
}
barva_oci = {
    "modra":"TTGTGGTGGC",
    "zelena":"GGGAGGTGGC",
    "rjava":"AAGTAGTGAC"
}
spol = {
    "moski":"TGCAGGAACTTC",
    "zenska":"TGAAGGACCTTC"
}
rasa = {
    "belec":"AAAACCTCA",
    "crnec":"CGACTACAG",
    "azijec":"CGCGGGCCG"
}

dna = open("dna.txt", "r").read()

if (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["korencek"]) != -1 and dna.find(barva_oci["rjava"]) != -1) and dna.find(oblika_obraza["okrogel"]) != -1:
    print ("Bil je Žiga!")
elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["crna"]) != -1 and dna.find(barva_oci["modra"]) != -1 and dna.find(oblika_obraza["ovalen"]) != -1):
    print ("Bil je Matej!")
elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["rjava"]) != -1 and dna.find(barva_oci["zelena"]) != -1 and dna.find(oblika_obraza["kvadraten"]) != -1):
    print ("Bil je Miha!")
else :
    print ("Krivca ni med osumljenci..")
