# 0x0C. Python - Almost a circle
In this project i reviewed the following concepts:
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class Method
* Static Method
* Inheritance
* Unittest
* Read/Write file
I also learnt new concepts:
* args and kwargs
* Serialization/Deserialization
* JSON

# args and kwargs in python
Only the * (aesteric) is required in writing *args and **kwargs in python. The rest of the words args and kwargs is just a naming convention.
#(*args)
They are mostly used in function definitions. They allow you to pass a variable number of arguments to a function. When unsure of how many arguments can be passed to your function by user so the two keywords are used. *args is used to send a non-keyworded variable length list to the function.
# syntax
def test(f_arg, *var):
	print("first normal argument:", f_arg)
	for arg in var:
		print("another argument:", var)
# usage of kwargs
**kwargs allow you to pass keyworded variable length of arguments to a function. **kwargs should be used when you want to handle named arguments in a function.
def greet(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.iteritems():
			print("%s == %s" %(key, value)
The above are just example of usage of *args and **kwargs in handling keyworded arguments.
Using *args and **kwargs to call a function
So here we will see how to call a function using *args and **kwargs. Just consider that you have this little function:

def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3
Now you can use *args or **kwargs to pass arguments to this little function. Here’s how to do it:

# first with *args
>>> args = ("two", 3,5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two","arg1":5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
Order of using *args, **kwargs and formal args
So if you want to use all three of these in functions then the order is

some_func(fargs,*args,**kwargs)
