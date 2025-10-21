# Class Exercies

Requirements:
- Version all your work in git.
- Create a folder at the root of the project with your class 'eerial number** - it should be a double digit.  This is how the project root should look like:

```                                                  
./
├── 00
├── 01
├── 02
[...]
```
## 1. Hello user

Create a file: "user.py" and:

Write a program that asks for a user’s name and prints a welcome message, e.g.

```bash
> What is your name?
Welcome Dr. Alice, to Python for Bioinformatics!
```
## 2. Nucleotide Counter

Create a file: "nucleotiede_counter.py" and:

Ask the user for a DNA sequence (string).

Print the number of each nucleotide: A, T, G, C.
Example: Input: ATGCTTGA → Output: A=2, T=3, G=2, C=1

## 3. Reverse Complement:

Create a file: "reverse_complement.py** and:

Given a DNA string, print it's reverse complement.

Example:
GCAT -> ATGC

## 4. Extract all the gene names given a file:

Create a file: "extract_genome.py" and:

Given a file:

```test.txt
gene:BRCA1 organism:Homo sapiens
gene:TP53 organism:Homo sapiens
gene:MT-CO1 organism:Homo sapiens
```

Extract all the gene names and output the results to a comma separated file E.g:

```csv
BRCA1,TP53,MT-CO1
```

Make sure that you use user-input to get the path for the filename, and the path for the output csv file.

