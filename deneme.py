#!/usr/bin/env python
#-*- coding: utf-8 -*-



# Kutuphaneler import ediliyor
from pisi.db.filesdb import FilesDB
import re
import sys

# files_db sinifi ornekleniyor
files_db = FilesDB()
dosyalar = files_db.search_file("Config.cmake") +  files_db.search_file("*-config.cmake")

# kullanilacak listeler tanimlaniyor

deb_liste = []
deb_liste_parcali = []
bagimliliklar = []
arama_list = []
bulunanlar = []

# kullanilacak kumeler tanimlaniyor

bulunmayanlar = ()



# verilen cmakelists.txt ye ulasiliyor

cmake_list = sys.argv[1]


def cmake_ulas(): 
    # bu fonksiyon cmakelists in icerigini ulasilabilir hale getiriyor
    file_list = open(cmake_list , "r")
    
    parcali = file_list.read().split("find_package")
    parcali.pop(0)
    
    for i in parcali:
        
        deb_liste.append(i.split(")")[0].replace("(",""))

    for i in  deb_liste:
        
        deb_liste_parcali.append(i.strip("").split(" "))

def duzenle():
    #bu fonksiyon istenmeyen karekterlerden kurtuluyor
    for i in deb_liste_parcali:
        for j in i:
            if re.search("\$",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search("NO_MODULE",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search("EXACT",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search("OPTIONAL_COMPONENTS",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search("NO_POLICY_SCOPE",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search("QUIET",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search(".*CONFIG.*",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search(".*REQUIRED.*",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search(".*COMPONENTS.*",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.match("[0-9]",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if re.search("#",j):
                i.pop(i.index(j))
            elif j == "":
                i.pop(i.index(j))
        for j in i:
            if j == "":
                i.pop(i.index(j))
        
        bagimliliklar.append(i)





def bag_list():
    # bu fonksiyon bagimliliklari listeliyor
    
    # kullanilacak degiskenler tanimlaniyor
    
    ilk = True
    
    print "-----Bağımlılıklar listeleniyor-----"
    
    for i in bagimliliklar:
        if ilk == True:
            if i[0] not in arama_list:
                print i[0]
                arama_list.append(i[0])
                ilk = False
        n = 1
        if len(i) == 1:
            ilk = True
        while n < len(i) and len(i) != 1 :
            print i[0].strip("\n") + i[n].strip("\n")
            arama_list.append(i[0].strip("\n") + i[n].strip("\n"))
            n = n +1
            ilk = True




def dizin_list():
    # bu fonksiyon bulunan bagimliliklarin dizinlerini listeliyor
    print "-----Bağımlılıkların bulunduğu dizinler listeleniyor-----"
    for i in arama_list:
        for j in dosyalar:
            for t in j:
                if i in t[0]:
                    print i +"------------------>" + t[0]
                    bulunanlar.append(i)
def olmayan_list():
    #bu fonksiyon dizinleri bulunamayan bagimliliklari listeliyor
    print "-----Bulunamayanlar listeleniyor-----"
    bulunmayanlar = set(arama_list) - set(bulunanlar)

    for i in bulunmayanlar:
        print i
        
        
def calistir():
    # diger fonksiyonlari sirasi ile calistirir
    cmake_ulas()
    duzenle()
    bag_list()
    dizin_list()
    olmayan_list()


calistir()
                
           



    
    
    
    
    
    
    
    
    
    
