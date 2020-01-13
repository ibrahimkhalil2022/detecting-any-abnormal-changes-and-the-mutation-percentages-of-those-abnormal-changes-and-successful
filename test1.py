list1 = ['A', 'C', 'O', 'V']
list2 = ['A', 'C', 'G', 'T','G', 'A', 'C', 'A','O','V','D']

list3 = set(list1)&set(list2) 

list4 = filter(list3, list1)
#list4 = sorted(list3, key = lambda k : list1.index(k))

print('The Vowel are:')

for word in list4:
    print(word)
