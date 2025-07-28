#print
print("Test")
name = "Mike"
age = 30
print ("mike ", name , " is ", age, " years old", sep="|")
print("test\n")

#Help
# To get help on the print function, you can use the help function in Python.
help(print)

#range()
# The range function generates a sequence of numbers.
rng = range(1, 10, 2)  # Start at 1, end before 10, step by 
for i in rng:
    print(i)
    
#map()
# The map function applies a function to all items in an input list.
strings = ["1", "2", "3"]
numbers = map(int, strings)  # Convert strings to integers
for number in numbers:
    print(number)
    
#filter()
# The filter function filters items out of a list based on a condition.
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)  #Filter even numbers
for even in even_numbers:
    print(even)
    
#sum()
# The sum function returns the sum of all items in an iterable.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers, -10)  # Calculate the sum of the list
print("Total:", total)
#zip()
# The zip function combines multiple iterables into tuples.

#sorted()
# The sorted function returns a new sorted list from the items in an iterable.
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted:", sorted_numbers)
print(type(sorted_numbers))

#zip()
# The zip function combines multiple iterables into tuples.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = zip(names, ages)  # Combine names and ages
for name, age in combined:
    print(name, age)    
    
#open()
# The open function opens a file and returns a file object.
file_path = "example.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()  # Read the entire file
        print("File content:", content)
except FileNotFoundError:
    print(f"File {file_path} not found.")
    
#alternate using with
with open(file_path, "w") as file:
    file.write("Hello, World!")  # Write to the file
    print(f"Written to {file_path}")