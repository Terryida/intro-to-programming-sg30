#Create a file: "extract_genome.py" and Given a file, Extract all the gene names and output the results to a comma separated file E.g:
# Create a file
f = open("test.txt", "x")

# Read the input file
with open("test.txt") as f:
  print(f.read())

# Function to extract gene names
import re

# Input and output file paths
input_file = "test.txt"
output_file = "test.csv"

# Open and read the file
with open(input_file, 'r') as f:
    text = f.read()

# Use regex to find all occurrences of gene:<gene_name>
gene_names = re.findall(r'gene:([^\s]+)', text)

# Print the list of gene names
print(gene_names)

# Join the names with commas
csv_content = ",".join(gene_names)

# Write to output CSV file
with open(output_file, "w") as f:
    f.write(csv_content)

print(f"Extracted {len(gene_names)} gene names and saved to '{output_file}'.")
