# Python program to illustrate the intersection 
# of two lists, sublists and use of filter() 
def intersection(lst1, lst2): 
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    
    return lst3 
  
# Driver Code 
lst1 = ['A', 'C', 'G', 'T','G', 'A', 'C', 'A','O','V','D']
lst5 = ['A', 'C', 'O', 'V','H']
lst2 = ['A', 'C', 'O', 'V']
word = intersection(lst1, lst2)


for we in word:
    print(we)

def intersectionn(lst5, lst2): 
    lst6 = [list(filter(lambda x: x in lst5, sublist)) for sublist in lst2]
    
    return lst6
wordd = intersectionn(lst5, lst2)

new = intersection(word, wordd)
for we in wordd:
    print(we)

print("...........Percentage  Section..............")
common = len(word)
first = len(lst1)

print(common)
print(first)

main = (100 * common)/first
print(str(main) +"%")



