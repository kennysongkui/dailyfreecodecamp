'''
DNA Mutations
Given two DNA strands of equal length, return an array of indexes where the strands differ (mutations).

DNA strands are strings made up of the characters "A", "T", "C", and "G"
Return the indexes in ascending order
If there are no mutations, return an empty array

'''


def detect_mutations(strand1, strand2):
    dna_len = len(strand1)

    chars = []
    for i in range(dna_len):
        if strand1[i] != strand2[i]:
            chars.append(i)
        else:
            pass
    print(chars)

    strand1 = chars

    return strand1


t = detect_mutations("ATCG", "ATGG")
print(t)
