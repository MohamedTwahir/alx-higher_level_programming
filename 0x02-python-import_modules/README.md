# 0x02. Python - import & modules
Tasks:
* 0. Import a simple function from a simple file
* 1. My first toolbox!
* 2. How to make a script dynamic!
~ Write a program that prints the number of and the list of its arguments.

	* The output should be:
		^ Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
		^ : (or . if no arguments were passed) followed by
		^ a new line, followed by (if at least one argument),
		^ one line per argument:
			- the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
	* Your code should not be executed when imported
	* The number of elements of argv can be retrieved by using: len(argv)
	* You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
* 3. Infinite addition
~ Write a program that prints the result of the addition of all arguments

	* The output should be the result of the addition of all arguments, followed by a new line
	* You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
	*Your code should not be executed when imported
* 4. Who are you?
~ Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

	* You should print one name per line, in alpha order
	* You should print only names that do not start with __
	* Your code should not be executed when imported
	* Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)
* 5. Everything can be imported
~ Write a program that imports the variable a from the file variable_load_5.py and prints its value.

	* You are not allowed to use * for importing or __import__
	* Your code should not be executed when imported


