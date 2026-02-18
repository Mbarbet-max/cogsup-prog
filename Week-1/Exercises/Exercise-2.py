################################################################################
"""
Recommended readings: 
  https://docs.python.org/3/library/stdtypes.html#ranges
  https://pyformat.info/#number_padding 
"""
################################################################################

"""
Exercise 2.1

Task:
------
Write a for-loop that prints out the following line 20 times:
 All work and no play makes Jack a dull boy.
"""

print("Exercise 2.1")

counter1 = 0
for counter1 in range(20) :
  print('All work and no play makes Jack a dull boy.')
  counter1 += 1

print("---")
"""
Exercise 2.2

Task:
------
Write a for-loop that prints out the numbers from 0 up to 5 inclusive.
"""

print("Exercise 2.2")

counter2 = 0
for counter2 in range(6) :
   print(counter2)
   counter2 =+ 1

print("---")


"""
Exercise 2.3

Task:
------
Write a for-loop that prints out the EVEN numbers from 2 up to 8 inclusive.
"""

print("Exercise 2.3")

counter3 = 1
for counter3 in range(9) :
   if counter3 % 2 == 0:
      print(counter3)
      counter3 += 1

print("---")

"""
Exercise 2.4

Task:
------
Now write another loop to print 9 through 0 (i.e., backwards).
"""

print("Exercise 2.4")

counter4 = 9
for counter4 in range(9, -1, -1):
   if counter4 % 2 == 1 :
    print(counter4)
    counter4 -= 1

print("---")

"""
Exercise 2.5

Task:
------
Write code that prints out the following sequence:
 z
 zz
 zzz
 zzzz
 zzzzz
 zzzzzz
 zzzzzzz
 zzzzzzzz
"""

print("Exercise 2.5")

counter5 = 0
for counter5 in range(9) :
   print('z'*counter5)
   counter5 =+ 1

print("---")

"""
Exercise 2.6

Task:
------
Write code that prints out the following sequence WITHOUT initializing an empty string:
 1
 12
 123
 1234
 12345

Hint: The function print takes an argument called 'end', which specifies what
to print at the end of the input string. By default, this parameter is set to \n, 
which is why the script moves automatically to a new line after the execution
of a simple print-statement.
------
"""

print("Exercise 2.6")

counter6 = 1
for counter6 in range(1, 6):
  for i in range(1, counter6 + 1):
    print(i, end='')
  print()
  
  
print("---")

"""
Exercise 2.7

Task:
------
Write code that uses a variable called 'rows'. If 'row' is equal to 1, it should print:
  o

If rows equals 5, it should print:
     o
    ooo
   ooooo
  ooooooo
 ooooooooo

You should be able to give any value to row and see a triangle made out of 'o's. 

Hint: Before you start coding, think what set of instructions (algorithm) 
your code needs to carry out for a certain value of rows.
------
"""

print("Exercise 2.7")

rows = 5
nbr_o = 1
for counter7 in range(rows) :
  print(' ' * (rows - counter7 - 1) + 'o' * nbr_o)
  nbr_o += 2

print("---")

"""
Exercise 2.8

Task:
------
Write code that prints the multiplication table:
 1   2   3   4   5   6   7   8   9  10
 2   4   6   8  10  12  14  16  18  20
 3   6   9  12  15  18  21  24  27  30
 4   8  12  16  20  24  28  32  36  40
 5  10  15  20  25  30  35  40  45  50
 6  12  18  24  30  36  42  48  54  60
 7  14  21  28  35  42  49  56  63  70
 8  16  24  32  40  48  56  64  72  80
 9  18  27  36  45  54  63  72  81  90
 10  20  30  40  50  60  70  80  90 100

Hint: One of the two links at the top of this script contains helpful information
on how to align the numbers.
------
"""

print("Exercise 2.8")

for x in range(1, 11):
  print(''.join('{:4d}'.format(x*y) for y in range(1, 11)))

print("---")