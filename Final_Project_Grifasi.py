#!/usr/bin/env python
# coding: utf-8

# In[25]:


#
# 1) Necessary modules to import + info referenced later.
#
import os
import glob
#
# ATOMIC NAMES IN BASIS SET
H_ = 'hydrogen'
C_ = 'carbon'
N_ = 'nitrogen'
O_ = 'oxygen'
F_ = 'fluorine'
P_ = 'phosphorus'
S_ = 'sulfur'
Cl_ = 'chlorine'
As_ = 'arsenic'
Se_ = 'selenium'
Br_ = 'bromine'
#
# ATOMIC NUMBERS IN BASIS SET
H = '1'
C = '6'
N = '7'
O = '8'
F = '9'
P = '15'
S = '16'
Cl = '17'
As = '33'
Se = '34'
Br = '35'
#
# 2) Mapping files for data extraction.
#
xyz_data = os.path.abspath ('C:\\Users\\agrif\\Desktop\\Research\\EFP\\Benchmark References\\Ref #2 xyz\\*.xyz')
data_files = glob.glob(xyz_data)
#
# 3) Mapping template EFP file.
#
makefp_template = os.path.abspath ('C:\\Users\\agrif\\Desktop\\Research\\EFP\\MakeEFP_Template.txt')
#
# 4) Dividing up lines in xyz files for extraction + manipulation.
#    - 'system_name'  =    name of molecule
#    - 'coords'       =    coordinate data of atoms in molecule
#
for file in data_files:
    readfile = open(file, 'r')
    data = readfile.readlines()
    base = os.path.basename(file)
    system_name = os.path.splitext(base)[0]
    coords = data[2:]
#
#
# 5) - If there is 'this' atom in coordinate data, print atomic name (for later writing to EFP files).
#    - If 'this' atom is not in coordinate data, instead print 'null'.
#    - Join atom names together and remove all 'null' values.
#
    if 'H ' in str(coords):
        H_name = (H_)
    else:
        H_name = 'null'
    if 'C ' in str(coords):
        C_name = (C_)
    else:
        C_name = 'null'
    if 'N ' in str(coords):
        N_name = (N_)
    else:
        N_name = 'null'
    if 'O ' in str(coords):
        O_name = (O_)
    else:
        O_name = 'null'
    if 'F ' in str(coords):
        F_name = (F_)
    else:
        F_name = 'null'
    if 'P ' in str(coords):
        P_name = (P_)
    else:
        P_name = 'null'
    if 'S ' in str(coords):
        S_name = (S_)
    else:
        S_name = 'null'
    if 'Cl ' in str(coords):
        Cl_name = (Cl_)
    else:
        Cl_name = 'null'
    if 'As ' in str(coords):
        As_name = (As_)
    else:
        As_name = 'null'
    if 'Se ' in str(coords):
        Se_name = (Se_)
    else:
        Se_name = 'null'
    if 'Br ' in str(coords):
        Br_name = (Br_)
    else:
        Br_name = 'null'
    atom_names = (H_name, C_name, N_name, O_name, F_name, P_name, S_name, Cl_name, As_name, Se_name, Br_name)
    atom_names_joined = ', '.join(atom_names)
    atom_names_cleaned = (atom_names_joined.replace('null, ', '').replace(', null', ''))
#
#
# 6) If there is 'this' atom in coordinate data, add atomic number to line (for later writing to EFP files.)
#
    coords_fixed = str(coords).replace('H ','H 1 ').replace('C ','C 6 ').replace('N ','N 7 ').replace('O ','O 8 ').replace('F ','F 9 ').replace('P ','P 15 ').replace('S ','S 16 ').replace('Cl ','Cl 17 ').replace('As ','As 33 ').replace('Se ','Se 34 ').replace('Br ', 'Br 35 ').replace('\\n','').replace("[",'').replace("]",'').replace("'",'').replace(", ",'\n')
#
#
# 7) For all xyz files in the specified location, replace template strings with real data and write to new EFP files.
#    - 'system_name' has the atom symbols in it, to be put in place of _X_.
#    - 'system_name' is the full molecule name, to be put in place of _Y_.
#    - 'coords' has the coordinate data in it, to be put in place of _Z_.
#
    with open("{}_EFP.inp".format(system_name), "w") as f:
        makefp_file = open(makefp_template, "r")
        new_file = ""
        for line in makefp_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace("_X_", atom_names_cleaned).replace("_Y_", system_name).replace("_Z_", coords_fixed)
            new_file += new_line +"\n"
        makefp_file.close()
        f.write(new_file)
        f.close()
#
readfile.close()
