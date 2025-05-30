# ===============================================================================
# Created on May 30, 2025
# 
# This file combines all the Python notebook exercises demonstrating:
# 1. Basic Data Types and Type Conversion
# 2. String Operations
# 3. Lists Operations
# 4. Tuples Operations  
# 5. Sets Operations
# ===============================================================================

print("🐍 Welcome to Python Fundamentals Collection! 🐍\n")

# ===============================================================================
# FILE 1: PYTHON BASICS - DATA TYPES AND TYPE CONVERSION (start.ipynb)
# ===============================================================================

"""
EXPLANATION:
This section covers Python's fundamental data types including integers, floats, 
complex numbers, strings, booleans, None type, and lists. It demonstrates how to 
check variable types using type() function and perform type conversions between 
different data types. It also shows basic user input handling and arithmetic operations.
"""

print("=" * 80)
print("SECTION 1: PYTHON BASICS - DATA TYPES AND TYPE CONVERSION")
print("=" * 80)

# Basic Data Types
a = 5 
print(a)
print(type(a))

b = 3j
print(b)
print(type(b))

c = 222.22
print(c)
print(type(c))

d = "hello world"
print(d)
print(type(d))

e = True
print(e)
print(type(e))

f = False
print(f)
print(type(f))

g = None
print(g)
print(type(g))

h = [1, 2, 3, 4, 5]
print(h)
print(type(h))

print('\n')

# Type Conversion
d = int(c)
print(d)
print(type(d))

e = float(a)
print(e)    
print(type(e))

print('\n')

cc = complex(a)
print(cc)
print(type(cc))

# User Input and Basic Operations
aa = input("Enter a number: ")
ss = int(aa)
print(ss+5)

print('\n')

bb = input("Enter a number: ")
kk = int(bb)
print(kk%5)

print('\n')

dd = input("Enter a number: ")
mm = int(dd)
print(mm/5)

ff = input("Enter a number: ")
nn = int(ff)
print(nn*5)

"""
SUMMARY OF SECTION 1:
- Demonstrated all basic Python data types (int, float, complex, str, bool, None, list)
- Showed how to check types using type() function
- Performed type conversions between different data types
- Illustrated basic user input handling and arithmetic operations
- Key takeaway: Python is dynamically typed and provides easy type conversion methods
"""

# ===============================================================================
# FILE 2: PYTHON STRING OPERATIONS (second.ipynb)
# ===============================================================================

"""
EXPLANATION:
This section focuses on string manipulation in Python. It demonstrates various 
string methods for case conversion, text cleaning, replacement, splitting, and 
counting occurrences. These operations are fundamental for text processing and 
data cleaning tasks in Python programming.
"""

print("\n" + "=" * 80)
print("SECTION 2: PYTHON STRING OPERATIONS")
print("=" * 80)

# Getting User Input
a = input("Enter a String: ")
print(a)
b = input("Enter a String: ")
print(b)

# String Case Conversion Methods
print(a.upper())

print(a.lower())

print(a.capitalize())

print(a.strip())

# String Manipulation Methods
print(a)

print(a.replace("a", "b"))

print(a.split("a"))

print(a.split(" "))

print(a.count("a"))

"""
SUMMARY OF SECTION 2:
- Demonstrated string case conversion methods (upper, lower, capitalize, strip)
- Showed string manipulation techniques (replace, split, count)
- These methods are essential for text processing and data cleaning
- Key takeaway: Python provides rich string manipulation capabilities out of the box
"""

# ===============================================================================
# FILE 3: PYTHON LISTS TUTORIAL (list.ipynb)
# ===============================================================================

"""
EXPLANATION:
This section covers Python lists, which are ordered, mutable collections that can 
hold different data types. It demonstrates list creation, indexing, slicing, 
concatenation, and various list methods. Lists are one of the most important 
data structures in Python for storing and manipulating sequences of data.
"""

print("\n" + "=" * 80)
print("SECTION 3: PYTHON LISTS TUTORIAL")
print("=" * 80)

# Creating Lists
my_list = ['orange', 'mango', 'banana', 'apple']
print(my_list)
print(type(my_list))

# List Slicing
print(my_list[3:5])

# Creating and Concatenating Lists
my_list2 = ['two','three']

print(*(my_list + my_list2), sep ='\n')

# Adding Elements to Lists
my_list2.append('five')

my_list2.insert(0, 'one')
my_list2.insert(1, 'two')

# List Methods - Count and Index
print (my_list2.count('five'))
print (my_list2.count('one'))
print (my_list2.count('two'))

print (my_list2.index('five'))

# Extending Lists
my_list.extend(my_list2)
print(my_list)

"""
SUMMARY OF SECTION 3:
- Demonstrated list creation and basic operations
- Showed list slicing and indexing techniques
- Covered list methods: append(), insert(), count(), index(), extend()
- Illustrated list concatenation and modification
- Key takeaway: Lists are mutable and provide many built-in methods for manipulation
"""

# ===============================================================================
# FILE 4: PYTHON TUPLES TUTORIAL (tuples.ipynb)
# ===============================================================================

"""
EXPLANATION:
This section covers Python tuples, which are ordered, immutable collections. 
Unlike lists, tuples cannot be modified after creation, making them useful for 
storing data that shouldn't change. It demonstrates tuple creation, accessing 
elements, methods, concatenation, and conversion between tuples and lists.
"""

print("\n" + "=" * 80)
print("SECTION 4: PYTHON TUPLES TUTORIAL")
print("=" * 80)

# Tuple Basics
my_tuple = ('orange', 'mango', 'banana', 'apple')
print("\n--- Tuple Basics ---")
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

# Accessing Tuple Elements
print("\n--- Accessing Elements ---")
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])

# Modifying Tuples (Converting to List and Back)
duplicat_list = list(my_tuple)

duplicat_list.append('kiwi')
duplicat_list.insert(0, 'xyz')

updated_tuple = tuple(duplicat_list)
print(updated_tuple)

# Tuple Methods
print("\n--- Tuple Methods ---")
repeated_tuple = (1, 2, 3, 1, 2, 1)
print(repeated_tuple.count(1))
print(repeated_tuple.index(2))

# Tuple Concatenation
print("\n--- Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
combined = tuple1 + tuple2
print(combined)

# Nested Tuples
print("\n--- Nested Tuples ---")
nested = ((1, 2), ('a', 'b'), (True, False))
print(nested)
print(nested[1][0])

# Type Conversions
print("\n--- Conversions ---")
list_to_convert = ['one', 'two', 'three']

converted_tuple = tuple(list_to_convert)
print(f"List {list_to_convert} converted to tuple: {converted_tuple}")
back_to_list = list(converted_tuple)
print(f"Tuple converted back to list: {back_to_list}")

# Printing Tuple Elements
print("\n--- Printing Tuple Elements Line by Line ---")
print(*my_tuple, sep='\n')

"""
SUMMARY OF SECTION 4:
- Demonstrated tuple creation and immutability
- Showed tuple indexing and slicing operations
- Covered tuple methods: count() and index()
- Illustrated tuple concatenation and nesting
- Showed conversion between tuples and lists
- Key takeaway: Tuples are immutable but can be converted to lists for modification
"""

# ===============================================================================
# FILE 5: PYTHON SETS TUTORIAL (set.ipynb)
# ===============================================================================

"""
EXPLANATION:
This section covers Python sets, which are unordered collections of unique elements. 
Sets are useful for removing duplicates, membership testing, and mathematical 
set operations like union, intersection, and difference. It also covers frozensets, 
which are immutable versions of sets.
"""

print("\n" + "=" * 80)
print("SECTION 5: PYTHON SETS TUTORIAL")
print("=" * 80)

# Creating Sets
print("\n--- Creating Sets ---")
set1 = {1, 2, 3, 4}
set2 = set(["apple", "banana", "cherry"])
empty_set = set()
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Empty Set: {empty_set}")

# Adding Elements to Sets
print("\n--- Adding Elements ---")
set1.add(5)
set1.update([6, 7, 8])
print(f"Set1 after adding elements: {set1}")

# Removing Elements from Sets
print("\n--- Removing Elements ---")
set1.discard(8)
set1.remove(7)
print(f"Set1 after removing elements: {set1}")

# Accessing Elements in Sets
print("\n--- Accessing Elements ---")
for item in set2:
    print(item)

# Set Operations
print("\n--- Set Operations ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")

# Clearing Sets
print("\n--- Clearing a Set ---")
set1.clear()
print(f"Set1 after clearing: {set1}")

# Frozensets (Immutable Sets)
print("\n--- Frozenset (Immutable Set) ---")
frozen = frozenset([1, 2, 3])
print(f"Frozenset: {frozen}")

"""
SUMMARY OF SECTION 5:
- Demonstrated set creation and unique element property
- Showed adding and removing elements from sets
- Covered set operations: union, intersection, difference
- Illustrated set iteration and clearing
- Introduced frozensets as immutable sets
- Key takeaway: Sets are perfect for unique collections and mathematical set operations
"""

