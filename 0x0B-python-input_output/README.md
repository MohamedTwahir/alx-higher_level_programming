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
