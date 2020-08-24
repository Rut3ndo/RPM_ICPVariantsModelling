"""
Program:    Domain
File:       domain.py

Version:    V1.0
Date:       24.08.2020
Function:   

Copyright:  (c) Rutendo Mapeta, Birkbeck 2020 
Author:     Rutendo Mapeta, Birkbeck 
         
--------------------------------------------------------------------------

This program is released under the GNU Public Licence (GPL V3)

--------------------------------------------------------------------------
Description:
============
Script to assign residue positions to functional domains

--------------------------------------------------------------------------
Usage:
======
This file takes a txt file input based on user choice.
The text file is addressed form he config.txt file.
Once the Domain to search has been selected this function loops through the input text file checking against conditions set inside of the config.py file.
if a match is made then the matching location is returned.
--------------------------------------------------------------------------
Revision History:
=================
V1.0   24.08.20   Original   By: ACRM
"""


import config

def isit(choice):
 #   choice = input("Entre your search term>")
    count = 0
    for i in range(1, len(check)+1):
        if int(choice) in range(check[count],check[count+1]):
            print(choice," Found at;", check[count+2])
            count += 3
        count += 3
        if count > 53:
            break      

choice =input("ABCB4 or ABCB11;\n")
if choice   == "ABCB11":
    check   =   config.check_ABCB11
    file    =   config.ABCB11
elif choice == "ABCB4":
    check   =   config.check_ABCB4
    file    =   config.ABCB4
else:
    print("Bad choice")


f = open(file)
inputfile = (f.readlines())

for line in inputfile:
    stripped_line = line.strip()
    print(stripped_line)
    isit(stripped_line)