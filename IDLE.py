Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> qwertyuiop
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    qwertyuiop
NameError: name 'qwertyuiop' is not defined
>>> QWERTYUIOP
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    QWERTYUIOP
NameError: name 'QWERTYUIOP' is not defined
>>> 1+!
SyntaxError: invalid syntax
>>> 1+1
2
>>> 5/4
1.25
>>> 5//4
1
>>> 9/6
1.5
>>> 
KeyboardInterrupt
>>> a=5
>>> a
5
>>> a=5.3
>>> a
5.3
>>> a="Hello world"
>>> a
'Hello world'
>>> a='Hello world2"
SyntaxError: EOL while scanning string literal
>>> a='Hello world2'
>>> a
'Hello world2'
>>> a=5
>>> b=8.9
>>> a+b
13.9
>>> a=0o157
>>> a
111
>>> a=0O157
a
>>> 
>>> a
111
>>> a=0x456
>>> a
1110
>>> a=0X456
a
>>> 
>>> a
1110
>>> 6**8
1679616
>>> 3**4
81
>>> a="eunwoo"
>>> a
'eunwoo'
>>> a=eunwoo
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a=eunwoo
NameError: name 'eunwoo' is not defined
a
>>> 
>>> a="eunwoo's book"
>>> a
"eunwoo's book"
>>> a='eunwoo's book'
SyntaxError: invalid syntax
>>> mul="Life is good\n you need python"
>>> mul
'Life is good\n you need python'
>>> print (mul)
Life is good
 you need python
>>> head = "python"
>>> head
'python'
>>> tail = "is fun"
>>> tail
'is fun'
>>> head+tail
'pythonis fun'
>>> head*3
'pythonpythonpython'
>>> len(head)
6
>>> len(tail)
6
>>> a="life is too short, you need python!"
>>> a
'life is too short, you need python!'
>>> a[5]
'i'
>>> a[0]
'l'
>>> a[9]
'o'
>>> a[15]
'r'
>>> a[40]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a[40]
IndexError: string index out of range
>>> len(a)
35
>>> a
'life is too short, you need python!'
>>> a[0:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[0:3]
'lif'
>>> a[0:4]
'life'
>>> a="20210726.sunny"
>>> a
'20210726.sunny'
>>> date=a[0:9]
>>> date
'20210726.'
>>> date=a[0:8]
>>> date
'20210726'
>>> weather=a[10:15]
>>> weather
'unny'
>>> weather=a[9:15]
>>> weather
'sunny'
>>> date2=a[:8]
>>> date2
'20210726'
>>> weather2=a[9:]
>>> weather2
'sunny'
>>> q=pithon
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    q=pithon
NameError: name 'pithon' is not defined
>>> q
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> q="pithon"
>>> q
'pithon'
>>> q[1]='y'
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    q[1]='y'
TypeError: 'str' object does not support item assignment
>>> q[2]=y
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    q[2]=y
NameError: name 'y' is not defined
>>> q[:1]+'y'+q[2:]
'python'
>>> "i eat %d apples." %3
'i eat 3 apples.'
>>> "i eat %s apples." %"five"
'i eat five apples.'
>>> number=4
>>> number
4
>>> "i eat %d apples" %number
'i eat 4 apples'
>>> num=10
>>> day="three"
>>> num
10
>>> day
'three'
>>> "i ate %d apple, so i was sick for %s days." %(num, day)
'i ate 10 apple, so i was sick for three days.'
>>> place="home"
>>> howmuch="3000"
>>> what="go"
>>> "i want to %s %s as %d" %(what, place, howmuch)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    "i want to %s %s as %d" %(what, place, howmuch)
TypeError: %d format: a number is required, not str
>>> place="home"
>>> howmuch=3000
>>> what="go"
>>> "i want to %s %s as %d" %(what, place, howmuch)
'i want to go home as 3000'
>>> place="home"
>>> howmuch=3000
>>> what="go"
>>> "i want to %s %s %d" %(what, place, howmuch)
'i want to go home 3000'
>>> 