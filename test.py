# list of sequences
sequences = ['A', 'C', 'G', 'T','G', 'A', 'C', 'A','O','V','D']

# function that filters vowels
def filterAminoacid(sequence):
    Aminoacid = ['A', 'C', 'O', 'V']

    if(sequence in Aminoacid):
        return True
    else:
        return False

filteredAminoacid= filter(filterAminoacid, sequences)

print('The filtered Aminoacid are:')
for Aminoacid in filteredAminoacid:
    print(Aminoacid)
