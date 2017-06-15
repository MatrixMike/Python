Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
2
Hello!
5
Hello!
8
Hello!
11
Hello!
14
Hello!
17
Hello!
>>> 
>>> L=["RED","yellow","blue"]
>>> for color in L
SyntaxError: invalid syntax
>>> 
>>> for color in L;
SyntaxError: invalid syntax
>>> for color in L:
	print(color)

	
RED
yellow
blue
>>> print [0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print [0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> TypeError: 'builtin_function_or_method' object is not subscriptable
SyntaxError: invalid syntax
>>> 
>>> print L[0]
SyntaxError: invalid syntax
>>> print(L[0])
RED
>>> 
