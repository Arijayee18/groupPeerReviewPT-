'''
Ari'Jaye Derritt
Section J
References: TA Tammy 
Time: 4 hours
'''

def dna_to_rna(sequence):
    dna = ['A','T','G','C']
    rna = ''
    for i in range(len(sequence)):
        if sequence[i] == dna[0]:
            rna += 'U'
        elif sequence[i] == dna[1]:
            rna += 'A'
        elif sequence[i] == dna[2]:
            rna +='C'
        elif sequence[i] == dna[3]:
            rna += 'G'
    print(rna)
    return rna

def proteinSequence(rna):
    acids = []
    stopCondon = len(rna)
    startCondon = rna.find('AUG')
    proteinSequence = rna[startCondon:stopCondon]
    for i in range(0,len(proteinSequence),3):
        protiens = proteinSequence[i:i+3]
        if 'UAA' == protiens or 'UAG' == protiens or 'UGA' == protiens:
           break
        acids.append(protiens)

    print(acids)

    return acids


def parse_file_into_acids(filename):
    acidArray = []
    infile = open(filename, "r")
    for line in infile:
      line = line.strip()
      values = line.split()
      acidArray.append(values)
    return acidArray

def shortname(data,acids):
  shortname = ''
  for acid in acids:
      for values in range(len(data)):
        if acid == data[values][0]:
            shortname +=data[values][2]  
  print(shortname)
  return shortname

def test_my_functions():
   assert dna_to_rna("A") == "U"
   assert dna_to_rna("CGTAAGCT") == "GCAUUCGA"
   assert dna_to_rna("CGTAAGCT") == "GCAUUCGA"

if __name__ == '__main__':
    filename = input("FILE> ")
    sequence = input('SEQUENCE> ')
    rna = dna_to_rna(sequence)
    acids = proteinSequence(rna)
    data = parse_file_into_acids(filename)
    print('OUTPUT',shortname(data,acids))
