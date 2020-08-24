"""
Program:    Needle Pairwise.py
File:       needle_pairwise.py

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
This program will provide you the updated sequence position and change, after accounting for gaps in allignment.
This is currently running based on the output from the EMBOSS pairwise alignment from EBI website
This program is intended to remove human error when counting mutations and changes made from deletions and insertions.
This is intended to be used as an aid for mapping residues between sequences/pdbs.
--------------------------------------------------------------------------
Usage:
======
To use tun the following command from the CMD line;
python Refactor_needle_pairwisemaping.py ../FastaFiles/6c0v_abcb11_needle.txt 300

--------------------------------------------------------------------------
Revision History:
=================
V1.0   24.08.20   Original   By: RPM
"""
#*****************************************************************************
# Import Libarys
import sys
import re
#*****************************************************************************
#  Set up global variables 
regex_match     =   []
regex_string    =   ''
var_c           =   []
counter         =   0
var_gap         =   0
var_window      =   []
var_m           =   0
dict_h          =   {} #superimportant, links the two positions
dict_r2         =   {}
dict_h2         =   {}
var_j           =   ()

#*****************************************************************************
def reset_global_variables():
    """
    Resets all global variables used for searchs

    Return:     ---Nothing to return
    """
    global  regex_match, var_c, counter, var_gap, var_window
    regex_match    = []
    var_c    = []
    counter   =  0
    var_gap  =   0
    var_window   =   []
#*****************************************************************************
def extract_info(alignment_regex, align_pair, group):    
    """
    This function retrieves the seq_id and the sequence from the emboss needle alignment output
    It takes in the regular expression,the aligned pair of sequences and the group
    It returns a result from the "finditer" method.
    The output is an iterator where matches are returned in the order found.
   
    Args:
    seq_id_regex         --- this is a regular expression object in a variable
    e.g (seq_id_regex = re.compile(r'^(# 1: (\w+))', re.M))
                                    
    align_pair            --- this is the alignment file as it is read in 
    
    group                 --- this is the group of the regex containing the sequence
                                    
    Return:
    iterator of the matches     --- this is an object containing the regex matches 
    """
    re_alignment = []
    re_output_alignment = alignment_regex.finditer(align_pair)
    for matches in re_output_alignment:
        re_alignment.append(matches.group(group))
    return re_alignment

#   Read in file
#*****************************************************************************
with open(sys.argv[1], "r") as f:
    align_pair = f.read()
searcher =re.compile(r'^(# 1: (\w+))', re.M)
term = extract_info(searcher, align_pair, 2)

alignment_regex = re.compile(r'^([^#])({}\s+\d+\s\S+ |{}\W+\s\S+)(\S+|\s+)\d+.\D+(\w+\s+\d+\s\S+)'.format(term[0], term[0]), re.M)

#   sequence A File 
#*****************************************************************************
re_b11_seq = extract_info(alignment_regex, align_pair, 2)
reset_global_variables()
regex_string = re.compile(r'(\w+\s+\d+\s)([^,]+)')
for i in re_b11_seq:
    regex_match = extract_info(regex_string,i,2)
    var_c += ''.join(str(v) for v in regex_match)
abcb11 = "".join(var_c)

#   sequence B file              
#*****************************************************************************
re_6cov_seq = extract_info(alignment_regex, align_pair, 4)
reset_global_variables()
for i in re_6cov_seq:
    regex_match = extract_info(regex_string,i,2)
    var_c += ''.join(str(v) for v in regex_match)
pdb_6cov = "".join(var_c)

#*****************************************************************************
var4 = [i.replace("\n", "") for i in abcb11]
var4 = ''.join(var4)

var3 = [i.replace("\n", "") for i in pdb_6cov]
var3 = ''.join(var3)

keys = range(0,len(var4))
values = var3
d3 = dict(zip(keys, values))

keys1 = range(0,len(var4))
values2 = var4
d4 = dict(zip(keys1, values2))

#   Data from Sequence A                
#*****************************************************************************
no_gap_seqA = {k:v for k,v in d3.items() if v != '-'}     #   Sequence A with all Gaps/deletions
gaps_seqA = {k:v for k,v in d3.items() if v == '-'}   #   All Gaps/deletions from sequence A

#  Data from Sequence B               
#*****************************************************************************
other_dict = {k:v for k,v in d4.items() if v != '-'}    #   Sequence B with all Gaps/deletions
gap6c0v_dict = {k:v for k,v in d4.items() if v == '-'}  #   All Gaps/deletions from sequence B
##      These dictonarys are interchangable, left over from the origianl developlment work

#   Counting the missing data      
#*****************************************************************************
reset_global_variables()
var_gap += 1
for k,v in no_gap_seqA.items():
    counter += 1
    dict_h[k] = counter
    var_gap += v.count("-")
    var_j += counter, k
    var_window.append(var_gap)

reset_global_variables()
for k,v in d4.items():
    counter += 1
    dict_h2[k] = counter
    var_gap += v.count("-")
    var_window.append(var_gap)
    dict_r2[counter] = var_gap


res_pos1 = sys.argv[2]
res_pos = int(res_pos1)-1
for i,res in enumerate(var4):
    try:
        w = (i for i in  gaps_seqA.keys())
    except:
        if res_pos == True:
            var_m = h[res_pos]            
for i in dict_h.keys():
    if res_pos == i:
        print(dict_h[res_pos] +   (dict_r2[res_pos])    )
    if res_pos == i:
        print(d3[res_pos      +   (dict_r2[res_pos])    ])
if res_pos in gaps_seqA.keys():
    print(gap6c0v_dict.values())