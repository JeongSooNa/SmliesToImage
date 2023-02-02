import os
import sys
from csv import reader
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import Draw

#############################
# Smiles to Images(png) file#
# to using RDKit Packages   #
# Create At 2023.02.01      #
# Update At 2023.02.02      #
# JSNA                      #
# smiles format is in csv   #
#############################

### input parameter
### input smiles csv
### column : index / name / smiles
input = sys.argv[1]
### output path
output = sys.argv[2]


if not os.path.exists(output):
        os.mkdir(output)

with open(input,'r') as csv:
        data = reader(csv)
        header = next(data)
        for row in data:
                index = row[0].split('\t')[0] # index
                name = row[0].split('\t')[1] # name
                smiles = row[0].split('\t')[2] # smiles
#               print(smiles)
                mol = Chem.MolFromSmiles(smiles)
                if mol != None:
                        img = Draw.MolToImage(mol,size=(300,300))
                        img.save(output + name)

##########################################################
####### When this Error Massage pops up, Complete! #######
##########################################################
#       Traceback (most recent call last):               #
#         File "SmilesToImages.py", line 31, in <module> #
#           index = row[0].split('\t')[0] # index        #
#       IndexError: list index out of range              #
##########################################################