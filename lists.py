# Simple List
animals = ['cat', 'dog', 'duck']
print(animals[2] + " to " + animals[-1])
animals[0] = 'koala'
animals.append('cat')
print(animals)
animals.insert(1,'horse')
del animals[-1]
print(str(animals) + " = " + str(len(animals)) + " items")
for animal in animals:
    if(animal == "duck"):
        print(animal)
print(list(range(0,5)))
#Item by item
numbers = []
for i in range(0, 6):
    numbers.append(i**2)
#List comprehension
squares = [num**2 for num in range(0,6)]
#Slices
my_slice=squares[1:3]
#Copy
my_other_slices = my_slice[:]
#Tuples are just inmutable lists
my_tuple = ("hey", "there", "freak")

