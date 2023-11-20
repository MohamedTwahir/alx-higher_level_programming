# 0x05. Python - Exceptions
This particular directory contains task done with an intention of mastering the python concept of exceptions.
Resources were shared as per usual protocol in learning the new concepts.
# Why Python programming is awesome
In my own perspective i find python awesome since it easy to learn and its expressions and always in simplest human readable format.
# What is the difference between errors and exceptions
* Errors can be defined as events or conditions that disrupt normal flow of a program. Although errors and exceptions are related concepts but their difference comes in play whether the error is detected before execution or while an execution occurs.
* Errors can be of many forms:
	* Syntax Errors or parse errors
	* Runtime Errors
* Exceptions:
	* Runtime Exceptions: These are exceptional events that occur during the execution of a program but are not necessarily errors. A good example can be attempting to open a file that doesnt exit or adding/converting  an integer to a string.
	* Handling Exceptions: this is where 'try' , 'except' keywords come in place.
# When do we need to use exceptions
Exceptions are a programming construct designed to handle unexpected or exceptional situations that can occur during the execution of a program. They provide a mechanism for gracefully responding to errors or exceptional conditions rather than allowing the program to terminate abruptly. Here are some situations where using exceptions is beneficial:

* Error Handling:

File Operations: When reading from or writing to files, exceptions can handle cases where the file is not found, permissions are insufficient, or there is an issue with the file format.
Network Operations: When dealing with network connections, exceptions can handle scenarios like timeouts, unreachable hosts, or data transmission errors.
* Input Validation:

User Input: When accepting user input, exceptions can be used to validate input and prompt the user to provide correct data.
Data Conversion: When converting data types, exceptions can catch errors such as attempting to convert a string to an integer when the string is not a valid number.
* Resource Management:

Memory Allocation: Exceptions can handle cases where memory allocation fails, preventing memory leaks and allowing for proper cleanup.
Database Operations: When working with databases, exceptions can handle issues like connection failures or SQL query errors.
* Robustness and Reliability:

External Dependencies: When interacting with external libraries or APIs, exceptions can gracefully handle unexpected behavior, ensuring that the program remains robust even in unpredictable scenarios.
Unforeseen Conditions: Exceptions provide a way to handle conditions that might not be anticipated during the development phase.
* Program Flow Control:

Custom Conditions: Developers can raise custom exceptions to signal specific conditions that require special handling. This can be useful for controlling the flow of the program.
* Debugging and Logging:

Debugging Information: Exceptions can be caught and logged, providing valuable information for debugging and diagnosing issues.
Error Reporting: Exceptions can be used to generate error reports that help developers understand the cause of problems in a production environment.
# How to raise a builtin exception
It is done so by using 'raise' statement. That statement is also used to generate an exception manually. 
Below is the basic syntax:
~ raise ExceptionType("Your error message")
In the above the 'ExceptionType' is the type of exception you want to raise.
# When do we need to implement a clean-up action after an exception
Cleaning up after an exception is important for maintaining the integrity of your program and its resources. Here are some scenarios where implementing a clean-up action after an exception is crucial:

~ Resource Release:

* File Handling: If your code involves opening files, it's essential to close them properly, even if an exception occurs. Failing to close files may lead to resource leaks.
* Network Connections: When working with network connections or sockets, you should close the connections in a finally block to ensure proper resource release.
* Database Connections: Similarly, when interacting with databases, close database connections in a finally block to release resources.
