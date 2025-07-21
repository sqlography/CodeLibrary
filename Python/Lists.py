#List is an ordered collection of elements
#0 Based
lst = [1, 2, 3, 4, 5]

#Access element by index
print(lst[0])  # Output: 1

#modify existing value 
lst[0] = 1000000

#print element based on reverse index
print(lst[-1]) #returns last element in the lst

#add element to the end
lst.append(5)
print(lst)

#remove element at specific inde
lst.pop(3)
print(lst)

#insert element at specific index
lst.insert(2, 1000)
print(lst)

#nesting lists
lst.append([6, 7, 8])
print(lst)

#extend list with another list
lst.extend([9, 10])
print(lst)

#lists are mutable and to copy
#don't use a list as a default paramete
lst = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(lst[0][2])  # Output: 3

#slicing lists
print(lst[:]) # Output: [1, 2, 3, 4, 5, 5, [6, 7, 8], 9, 10]
print(lst[1:4])  # Output: [2, 3, 4]
print(lst[1:5:2])  #

#check contains an element
print(3 in lst)  # Output: True

lst = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print(lst.count(5))  # Output: 2 (counts occurrences of 5)

print(lst.sort(reverse=True))  # Sorts the list in descending order
print(lst)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst)

lst2 = lst.copy()  # Creates a shallow copy of the list
print(lst2)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lst3 = lst[:]   
print(lst3)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))  # Combines names and ages into a list of
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

for x in lst:
    print(x, end=' ')  # Prints each element in the list on the same line
    
for x in lst:
    print(x)  # Prints each element in the list on a new line