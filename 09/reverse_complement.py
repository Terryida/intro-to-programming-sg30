#Create a file: "reverse_complement.py** and Given a DNA string, print it's reverse complement.
#Example: GCAT -> ATGC

from Bio.Seq import Seq

seq = Seq("TCGGGCCC")

print(f"My sequence is: {seq}")
print(f"The complementary sequence is:{seq.complement()}")
print(f"The reverse complement sequence is:{seq.reverse_complement()}")
