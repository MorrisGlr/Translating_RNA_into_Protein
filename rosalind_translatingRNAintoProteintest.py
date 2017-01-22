file = open('rosalind_prot.txt','r')
rawdata = file.readlines()
data = ''.join(rawdata)
#I extracted the data from a text file, converted it to a string. if I am looking
#at a a sequence in particular it is better to keep the sequence as a string
#becuase each character is assigned a unique index number. I did not use a list
#because it it groups all of the adenosines in a sequences under one index


codon_dict = {'UUU': 'F','CUU': 'L','AUU': 'I','GUU': 'V',
              'UUC': 'F','CUC': 'L','AUC': 'I','GUC': 'V',
              'UUA': 'L','CUA': 'L','AUA': 'I','GUA': 'V',
              'UUG': 'L','CUG': 'L','AUG': 'M','GUG': 'V',
              'UCU': 'S','CCU': 'P','ACU': 'T','GCU': 'A',
              'UCC': 'S','CCC': 'P','ACC': 'T','GCC': 'A',
              'UCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A',
              'UCG': 'S','CCG': 'P','ACG': 'T','GCG': 'A',
              'UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D',
              'UAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D',
              'UAA': 'Stop','CAA': 'Q','AAA': 'K','GAA': 'E',
              'UAG': 'Stop','CAG': 'Q','AAG': 'K','GAG': 'E',
              'UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G',
              'UGC': 'C','CGC': 'R','AGC': 'S','GGC': 'G',
              'UGA': 'Stop','CGA': 'R','AGA': 'R','GGA': 'G',
              'UGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G'}
#dictionary that will yeild amino acid according to codon sequences


upperlimit =len(data)+1
codonlist = []
stringindex = []
codon = []
for i in range(0, len(data)):
    stringindex.append(i)
for i in stringindex:
    count = 0
    insert = data[i]
    codon.append(insert)
    if len(codon)==3:
        joinedcodon = ''.join(codon)
        codonlist.append(joinedcodon)
        del codon[:]

translation =[]
for i in codonlist:
    aminoacid= codon_dict[i]
    if aminoacid !='Stop':
        translation.append(aminoacid)
print(''.join(translation))
