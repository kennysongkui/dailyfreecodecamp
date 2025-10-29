'''
Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
'''

def complementary_dna(strand):
    dna_dict = {"A":"T", "C":"G","T":"A", "G":"C"}
    new_list = []
    for i in strand:
        new_list.append(dna_dict[i])

    print(new_list)
    report = ''.join(new_list)
    strand = report

    return strand

t = complementary_dna("ATGCGTACGTTAGC")
print(t)