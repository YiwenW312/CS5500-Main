# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

For dictionary, most of the functions have good names, except for list(d), it would be better to be named as getList(d) since it returns a list, and pop(), as mentioned above, it could be named as popAndGet(), similar for popitem(). For list, all the functions have proper names.


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

For a dictionary it's based on hash table, and for a list it's based on dynamic array.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list allows for random access with index. 

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pro: 
It's more flexible, easier to reuse the code, easier to learn, and can reduce complexibility. 
Con:
It will not be so good in terms of performance, it's easier to introduce bugs, might have safty issue and can be misused. 

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

requests.get(): This function is well named

status_code: This function is well named

headers: This function is well named

encoding: This name could be better if it can indicate that it's the encoding of the response.

text: This attribute provides the response body as a string. It's not so clear.

json(): This function is well named

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

The class does have a large number of parameters, however, providing default values and keyword arguments can help reduce the confusion, and for some common use case, it can also mitigate the possibility of having errors. 

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

 `**kwargs` is a special syntax in Python for passing a variable number of keyword arguments to a function. The name kwargs stands for "keyword arguments". It can take any extra parameters. 

 Pros: it can be easier to use, more flexible, extensible, and it can provide cleaner interface. 
 Cons: it can cause ambiguity, easier to have errors, hard to document.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Optionality: By setting a default value (like None), the argument becomes optional. So it provides more flexibility.
Indication: It indicates that not having this parameter is ok for some scenarios.
Flexibility: It provides an options that users can choose what parameters to pass. 
Yes the arguments be set to other values besides "None"
Setting predetermined value can make it easier to use, improve the clearity.