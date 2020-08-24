"""
Program:    Domain
File:       config.py

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
Configuration file driving domain.py


--------------------------------------------------------------------------
Usage:
======
This is the config file for the Domain check function, Change the location of the text files that you want to run throught to ge the domain infomation.
There are two text files, abcb11.txt and abcb4.txt, examples provided.
--------------------------------------------------------------------------
Revision History:
=================
V1.0   24.08.20   Original   By: ACRM
"""



## Initiale location of txt files, adjust as required
ABCB11  =   ("../abcb11.txt")
ABCB4   =   ("../abcb4.txt")

## array with domain values to search from, values in the order;
##              Start, End, Domian ID, e.g. 62, 386, "TMD1"
check_ABCB11 = [  62,     386,    "TMD1",
            420,    657,    "NDB1",
            755,    1044,   "TMD2",
            1078,   1316,   "NDB2",
            58,     92,     "TH1",
            115,    185,    "TH2",
            195,    238,    "TH3",
            240,    287,    "TH4",
            297,    351,    "TH5",
            355,    398,    "TH6",
            738,    783,    "TH7",
            789,    842,    "TH8",
            854,    896,    "TH9",
            900,    946,    "TH10",
            956,    1009,   "TH11",
            1014,   1057,   "TH12",
            1,      1,      "FAKE", 
            1,      1,      "FAKE"
        ]

check_ABCB4 = [   57,     360,    "TMD1",
            394,    631,    "NDB1",
            711,    1000,   "TMD2",
            1034,   1280,   "NDB2",
            53,     87,     "TH1",
            115,    160,    "TH2",
            170,    213,    "TH3",
            215,    262,    "TH4" ,         
            272,    376,    "TH5",
            330,    372,    "TH6",
            707,    740,    "TH7" ,     
            746,    798,    "TH8",
            810,    852,    "TH9",
            856,    902,    "TH10",
            912,    965,    "TH11",
            970,    1013,   "TH12",
            1,      1,      "FAKE", 
            1,      1,      "FAKE"
        ]