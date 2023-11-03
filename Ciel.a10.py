#  Ciel Cochran
#  Assessment 10
#  Section J
#  Time:
#  References: none

# Function to transcribe a DNA sequence into RNA


def dna_to_rna(sequence):
    Transcription = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    rna = ''.join(Transcription[x] for x in sequence)
    # print(rna)
    return rna


# Function to parse the amino acid data file into a list


def parse_file_into_acids(filename):
    acids = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            acids.append(data)
    return acids

# Function to translate an RNA sequence into amino acids


def translate_rna_to_amino_acids(rna, codon_data):
    amino_acids = []
    start_codon = "AUG"
    stop_codons = {"UAA", "UGA", "UAG"}
    i = rna.index(start_codon)

    while i < len(rna):
        codon = rna[i:i+3]
        if codon == start_codon:
            amino_acids.append("M")
            i += 3
            # print('M')
        elif codon in stop_codons:
            break
        else:
            for acid in codon_data:
                if acid[0] == codon:
                    amino_acids.append(acid[2])
                    i += 3
                    # print(acid[2])
                    break
    # Join the amino acid letters into a single string
    amino_acid_sequence = "".join(amino_acids)

    return amino_acid_sequence


# Function to test the program with sample DNA sequences
def test_my_functions():
    assert dna_to_rna('A') == 'U'
    assert dna_to_rna('C') == 'G'
    assert dna_to_rna('G') == 'C'
    assert dna_to_rna('T') == 'A'


if __name__ == "__main__":
    file_name = input('Enter filename: ')
    sequence = input('Enter DNA sequence: ')
    rna = dna_to_rna(sequence)
    data = parse_file_into_acids(file_name)
    result = translate_rna_to_amino_acids(rna, data)

    print(f'OUTPUT {result}')
