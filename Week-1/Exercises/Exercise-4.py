################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

print(sum(dct.values()))

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

print(max(dct.values()))

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")

squared = {a : b**b for a, b in dct.items()}
print(squared)

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

for k, v in dct.items() :
    if v % 2 == 0 :
      print(k)

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")


dct_switch = {v:k for k, v in dct.items()}
print(dct_switch)


print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

str = 'ccctcctttttcc'
dict = {'c' : 0, 't' : 0}

for letter in str :
   if letter in dict:
      dict[letter] += 1

print(dict)

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

lst = []
for letter in responses :
   if letter in responses_mapping :
      lst.append(responses_mapping[letter])


print(lst)
      

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

dct1 = {'a': 1, 'b': 2}
dct2 = {'c': 3, 'd': 4}
dct3 = dct1 | dct2
print(dct3)


print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_animals = sorted(animals.keys())
sorted_animals_dict = {}
for animal in sorted_animals:
   sorted_animals_dict[animal] = animals[animal]

print(sorted_animals_dict)


print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_animals_dict = {}

for anim, nbr in sorted(animals.items(), key=lambda item: item[1]):
   sorted_animals_dict[anim] = nbr
print(sorted_animals_dict)

print("---")