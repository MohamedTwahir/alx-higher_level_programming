# 0x0B. Python - Input/Output
Output of a programm can be in human-readable form, or written to a file for future use.
So far i have encountered two ways of writing values(output): the expression statement and the print(). A third way am learning today is using the write() method of file objects; the standard output file can be referenced as sys.stdout.
# formatted outputs
* using formatted string literals
begin a string with f or F before the opening quotation mark or triple quotation mark. {} can be used as python expressions to refer to variables or literal values.
Syntax:
>>> year = 2023
>>> event = 'ELection'
>>> f'Results of the {year} {event}'
'Results of the 2023 Election
* using the str.format()
This method of strings requires more manual effort. {} are still used for variables
syntax:
>>> yes_votes = 42-572-654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
'42572654 YES votes 49.67%'

* changing display of string for debugging purposes
The repr() or str() is used to convert any value to a string for debugging purposes.
The str() is meant to return representation of values which are fairly human-readable.
The repr() is meant to generate representation which can be read by the interpreter(it will force a SyntaxError if no equivalent syntax)
For objects which don’t have a particular representation for human consumption, str() will return the same value as repr().
s = 'Hello, world.'
str(s)
'Hello, world.'
repr(s)
"'Hello, world.'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
The value of x is 32.5, and y is 40000...
The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
'hello, world\n'
The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
The string module contains a Template class that offers yet another way to substitute values into strings, using placeholders like $x and replacing them with values from a dictionary, but offers much less control of the formatting.
Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
* The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
# Other useful functions and their examples
* vars() - returns a dictionary containing all local variables.
* str.rjust() - right-justifies a string in a field of a given width by padding it with spaces on the left.
* str.ljust() & str.center() - do not write anything they just return a new strin
* str.zfill() - pads a numeric string on the left with zeros. It understands about plus and minus signs.
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
# Reading and Writing Files
open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)
>>> f = open('workfile', 'w', encoding="utf-8")

