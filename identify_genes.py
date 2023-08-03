import re

def identify_genes(dna_sequence):
  """Identifies genes in a DNA sequence.

  Args:
    dna_sequence: A string representing a DNA sequence.

  Returns:
    A list of strings, where each string represents a gene.
  """

  genes = []
  for match in re.finditer(r"ATG(.{3})*(TAA|TAG|TGA)", dna_sequence):
    gene = match.group()
    genes.append(gene)

  return genes


if __name__ == "__main__":
  dna_sequence = "ATGGGCTAACTAAGTAA"
  genes = identify_genes(dna_sequence)
  print(genes)
