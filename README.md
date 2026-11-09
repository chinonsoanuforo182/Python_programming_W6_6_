# W6_6

In this exercise, get familiar with the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) and specificly on the [ROT13](https://en.wikipedia.org/wiki/ROT13) implementation.

[Caesar Cipher explained](https://youtu.be/sMOZf4GN3oc)

| A |	B |	C |	D |	E |	F |	G |	H |	I |	J |	K |	L |	M |	N |	O |	P |	Q |	R |	S |	T |	U |	V |	W |	X |	Y |	Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N	| O	| P |	Q |	R |	S |	T |	U |	V |	W |	X |	Y |	Z |	A |	B |	C |	D |	E |	F |	G |	H |	I |	J |	K |	L |	M |  


In this exercise, you will implement a Caesar cipher using the ROT13 method.
* Create a Python program in a file named main.py.
* The program should:
  * Collect multiple lines of plain text from the user until an empty line is entered.
  * Apply ROT13 cipher to each line.
  * Ask for a filename to save the ciphered text.
  * Save the ciphered text to the given file.
  * If no filename is given, skip saving and print a message.

## ROT13 Cipher

ROT13 shifts each letter 13 positions forward in the alphabet. It must work for:

* Lowercase: abcdefghijklmnopqrstuvwxyz
* Uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ
* All other characters remain unchanged.


### Required Functions Overview

| Function Name | Purpose | Returns |
|---------------|---------|---------|
| `writeFile(Filename: str, Content: str)` | Saves the encrypted text to a file with the given filename | `None` |
| `askRows()` | Asks the user to input multiple lines of text (until an empty line is entered) | A single `str` containing all rows joined with newline characters |
| `shiftCharacter(Character: str, Alphabets: str, Shift: int = 13)` | Shifts a character by 13 positions in the given alphabet | A single shifted `str` character |
| `rot13(Content: str)` | Applies the ROT13 cipher to the input string | A new `str` with ROT13 applied |
| `main()` | Runs the full program: input, ciphering, output, and saving | `None` |


Run 1
````
Program starting.

Collecting plain text rows for ciphering.
Insert row(empty stops): Hello
Insert row(empty stops): World
Insert row(empty stops): 

#### Ciphered text ####
Uryyb
Jbeyq

#### Ciphered text ####
Insert filename to save: output.txt
Ciphered text saved!
Program ending.
````

Run 2
````
Program starting.

Collecting plain text rows for ciphering.
Insert row(empty stops): Veni
Insert row(empty stops): vidi
Insert row(empty stops): vici
Insert row(empty stops): 

#### Ciphered text ####
Irav
ivqv
ivpv

#### Ciphered text ####
Insert filename to save: output.txt
Ciphered text saved!
Program ending.
````

Run 3
````
Program starting.

Collecting plain text rows for ciphering.
Insert row(empty stops): Fortuna audaces iuvat.
Insert row(empty stops): Alea iacta est.
Insert row(empty stops): Gallia est omnis divisa in partes tres.
Insert row(empty stops): 

#### Ciphered text ####
Sbeghan nhqnprf vhing.
Nyrn vnpgn rfg.
Tnyyvn rfg bzavf qvivfn va cnegrf gerf.

#### Ciphered text ####
Insert filename to save: output.txt
Ciphered text saved!
Program ending.
````

Run 4
````
Program starting.

Collecting plain text rows for ciphering.
Insert row(empty stops): Hello
Insert row(empty stops): 

#### Ciphered text ####
Uryyb

#### Ciphered text ####
Insert filename to save: 
File name not defined.
Aborting save operation.
Program ending.
````
