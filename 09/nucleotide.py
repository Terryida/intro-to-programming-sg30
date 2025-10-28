#Create a file: "nucleotiede_counter.py" and Ask the user for a DNA sequence (string).
#Print the number of each nucleotide: A, T, G, C. Example: Input: ATGCTTGA → Output: A=2, T=3, G=2, C=1
def main():
    mysequence= input("Enter your DNA sequence: ")
    print(f"My DNA sequence is {mysequence}")
    a_count=mysequence.count("A")
    g_count=mysequence.count("G")
    c_count=mysequence.count("C")
    t_count=mysequence.count("T")

    print(f"A={a_count} ,G={g_count} ,C={c_count} ,T={t_count}")
main()
