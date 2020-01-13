# Python program to illustrate the intersection 
# of two lists, sublists and use of filter() 
def intersection(lst1, lst2): 
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    
    return lst3 
  
# Driver Code 
lst1 = ['A', 'C', 'O', 'V']
lst2 = [['A', 'C', 'G', 'T','G', 'A', 'C', 'A','O','V','D'],['A', 'C', 'O', 'V','H']]
word = intersection(lst1, lst2)


for we in word:
    print(we)


print("...........Percentage  Section..............")
common = len(word)
first = len(lst2)

print(common)
print(first)

main = (100 * common)/first
print(str(main) +"%")



