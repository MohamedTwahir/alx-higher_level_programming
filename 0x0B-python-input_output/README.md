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
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be:
* 'r' - file will only be read
* 'w' - for only writing(an existing file with the same name will be erased)
* 'a' - opens the file for appending; any data written to the file is automatically added to the end.
* 'r+' - opens the file for both reading and writing.
* 'b' - binary mode
Normally files are open in textmode, that means there is a specific encoding. Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you need to use a different encoding.
# With keyword
It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:
>>> with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it.
# Methods of File Objects
* f.read(size) - reads some quantity of data and returns it as a string. Size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned. Its your problem if the file is twice as large as your machine's memory. Otherwise at most size characters are read and returned. If end of the file has been reached, f.read() will return an empty string('')
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
* f.readline()
f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
One can loop over the file if there is a need for reading lines of the file.
>>> for line in f:
	print(line, end='')
If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
* f.write(string)
writes the contents of string to the file, returning the number of characters written.
>>> f.write('This is a test\n')
15
* f.tell()
returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

# Saving structured data with json
Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.
If you have an object x, you can view its JSON string representation with a simple line of code:
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'

Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

json.dump(x, f)

To decode the object again, if f is a binary file or text file object which has been opened for reading:

x = json.load(f)

