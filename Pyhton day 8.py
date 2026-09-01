
Set: In Python, a set is a collection used to store unique values.
A set is an unordered, mutable collection of unique elements in Python.
Example: 

a = {10, 20, 30, 20, 10}

print(a)
output: {10, 20, 30}
Main properties of set: 
1.Unordered — no fixed position/index.
2.No duplicates — every value is unique.
3.Mutable — you can add or remove elements.
4.No indexing — you cannot do a[0].

a = {10, 20, 30}

print(a[0])   # ❌ Error

Operations on set:

Union(): This method is used to combine two sets and return a new set with all unique elements from both sets.
syntax : set1.union(set2)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) or print(a.union(b))
output: {1, 2, 3, 4, 5}

Intersection(): This method is used to find the common elements between two sets and return a new set with those elements.
syntax : set1.intersection(set2)
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b) or print(a.intersection(b))
output: {3}

Difference(): This method is used to find the elements that are present in one set but not in the other and return a new set with those elements.
syntax : set1.difference(set2)
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b) or print(a.difference(b))
output: {1, 2}

Symmetric Difference(): This method is used to find the elements that are present in either of the sets but not in both and return a new set with those elements.
syntax : set1.symmetric_difference(set2)
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b) or print(a.symmetric_difference(b))
output: {1, 2, 4, 5}

Methods: 
1. add(): This method is used to add an element to the set.
syntax : set_name.add(value)
Example : 
a = {10, 20, 30}

a.add(40)

print(a)
output: {10, 20, 30, 40}
2. remove(): This method is used to remove the specified element from the set.
syntax : set_name.remove(value)
Example :
a = {10, 20, 30, 40}

a.remove(20)

print(a)
output: {10, 30, 40}

update(): This method is used to add multiple elements to the set.
syntax : set_name.update([value1, value2, value3])
Example1 :
a = {10, 20, 30}
a.update([40, 50, 60])
print(a)
output: {10, 20, 30, 40, 50, 60}

Example2 :
a = {10, 20, 30}
b = {40, 50, 60}
a.update(b)
print(a)
output: {10, 20, 30, 40, 50, 60}

discard(): This method is used to remove the specified element from the set if it exists. If the element does not exist, it does nothing.
syntax : set_name.discard(value)
Example1 :
a = {10, 20, 30, 40}
a.discard(20)
print(a)
output: {10, 30, 40}

Example2 :
a = {10, 20, 30, 40}
a.discard(50)
print(a)
output: {10, 20, 30, 40}

clear(): This method is used to remove all elements from the set.
syntax : set_name.clear()
Example :
a = {10, 20, 30, 40}
a.clear()
print(a)
output: set()
