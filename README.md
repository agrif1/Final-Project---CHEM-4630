# Final_Project_Grifasi

This is Alex Grifasi's final project for the CHEM 4630 course at CU Denver.
It is designed to take .xyz file exports from MacMolPlt and convert the pertinent data into a makefp.inp file ready for transfer to the GAMESS software package.

## Installation

1) Download and extract zip to folder of choice.

## Usage

1) Place any number of .xyz files in the 'input' folder.

2) Type into CMD.

	> python Final_Project_Grifasi.py

3) The following occurs.

	>> 'system_name' replaces _X_ in MakeEFP_Template.txt.

	>> 'system_name' replaces _Y_ in MakeEFP_Template.txt.

	>> 'coords' replaces _Z_ in MakeEFP_Template.txt.

	>>> output

4) Check 'output' folder for .inp files for GAMESS integration.

## Contributing

Derivations/additions to this script may include addition of atoms from differing basis sets.

## License
N/A