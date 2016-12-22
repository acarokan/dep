#!/usr/bin/env python
#-*- coding: utf-8 -*-




from pisi.db.filesdb import FilesDB
import re
import sys

files_db = FilesDB() 

cmake_list = sys.argv[1]
deb_liste = []
deb_liste_parcali = []
bagimliliklar = []
ilk = True
arama_list = []
file_list = open(cmake_list , "r")
parcali = file_list.read().split("find_package")
parcali.pop(0)


for i in parcali:
    deb_liste.append(i.split(")")[0].replace("(",""))


for i in  deb_liste:
        deb_liste_parcali.append(i.strip("").split(" "))
print deb_liste_parcali


print deb_liste_parcali
    
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
        if j == "":
            i.pop(i.index(j))
        
    bagimliliklar.append(i)

print "-----Bağımlılıklar listeleniyor-----"
for i in bagimliliklar:
    if ilk == True:
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


        

print "-----Bağımlılıkların bulunduğu dizinler listeleniyor-----"
for i in arama_list:
    for j in files_db.search_file(i):
        if i in j[1][0]:
            print i +"------------------>" + j[1][0]
           



    
    
    
    
    
    
    
    
    
    
