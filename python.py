Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> 1-2
-1
>>> a=1
>>> a
1
>>> b=3
>>> a+b
4
>>> a-b
-2
>>> a*b
3
>>> a/b
0.3333333333333333
>>> a//b
0
>>> a%b
1
>>> if a>1:
... print("a is greater than 1")
  File "<stdin>", line 2
    print("a is greater than 1")
    ^
IndentationError: expected an indented block
>>> if a>1:
...     print("a is greater than 1")
...
>>> if a>1:
...     print("a is greater than 1")
... a=2
  File "<stdin>", line 3
    a=2
    ^
SyntaxError: invalid syntax
>>> for a in [1,2,3]:
...     print(a)
...
1
2
3
>>> i=0
>>> while i<3:
...     i=i+1
...     print(i)
...
1
2
3
>>> def add (a,b):
...     return a+b
...
>>>
>>>
>>>
>>>
>>>
>>> add(3,4)
7
>>> a="""eunwoo's book"""
>>> a
"eunwoo's book"
>>> a='''eunwoo's book'''
>>> a
"eunwoo's book"
>>> a='''eunwoo book'''
>>> a
'eunwoo book'
>>>