# Junee Omana
# CSCI 128 - Section J
# Assessment 10
# References: no one
# Time: 1.5 hours

def parse_file_into_acids(filename):
    file = open(filename, "r")
    contents = file.read().splitlines()
    acid_list = []
    for line in contents:
        split = line.split(" ")
        acid_list.append(split)
    return acid_list

def dna_to_rna(sequence):
    rna_list = []
    for nucleotide in sequence:
        if nucleotide == "A":
            rna_list.append("U")
        if nucleotide == "T":
            rna_list.append("A")
        if nucleotide == "G":
            rna_list.append("C")
        if nucleotide == "C":
            rna_list.append("G")
    return "".join(rna_list)

def proteins(rna_sequence, acid_list):
    codon_list = []
    protein_list = []
    start = rna_sequence.index("AUG")
    for i in range(start, len(rna_sequence), 3):
        codon_list.append(rna_sequence[i:i + 3])
    for codon in codon_list:
        if codon == "UAA" or codon == "UGA" or codon == "UAG":
            return ''.join(protein_list)
        for acid in acid_list:
            if codon == acid[0]:
                protein_list.append(acid[2])

def test_my_functions():
    assert dna_to_rna("A") == "U"
    assert dna_to_rna("CGTAAGCT") == "GCAUUCGA"
    assert dna_to_rna("TTAAACCGGGCCCGGCTACCGACCCATGATTAAACCCTACTCAAATCATT") == "AAUUUGGCCCGGGCCGAUGGCUGGGUACUAAUUUGGGAUGAGUUUAGUAA"

if __name__ == "__main__":
    file = input("FILENAME> ")
    dna = input("SEQUENCE> ")
    rna = dna_to_rna(dna)
    acids = parse_file_into_acids(file)
    print(f'OUTPUT {proteins(rna, acids)}')
    test_my_functions()