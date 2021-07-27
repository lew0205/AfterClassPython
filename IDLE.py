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
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "Error is %d%%."%98
'Error is 98%.'
>>> "%s" %"hi"
'hi'
>>> "%10s" %"hi"
'        hi'
>>> "%-10s" "%hi"
'%-10s%hi'
>>> "%-10s" %"hi"
'hi        '
>>> "%-20s" %"hi"
'hi                  '
>>> "%-20s eunwoo" %"hi"
'hi                   eunwoo'
>>> "%0.4f" %3.25987654
'3.2599'
>>> "%10.4f" %3.25987654
'    3.2599'
>>> 
>>> "I eat {0} apples." .format(3)
'I eat 3 apples.'
>>> 
>>> "I eat {0} apples." .format("five")
'I eat five apples.'
>>> num=3
>>> "i eat {0} apples." .format(num)
'i eat 3 apples.'
>>> num=8
>>> day='three'
>>> num
8
>>> day
'three'
>>> "I eat {0} apples. so I was sick for {1} days." .format(num,day)
'I eat 8 apples. so I was sick for three days.'
>>> place="home"
>>> howmuch=3000
>>> what="go"
>>> "i want to {0} {1} {2}" .format(what, place, howmuch)
'i want to go home 3000'
>>> "i eat {num} apples. so i was sick for {day} days.".format(num=10,day=3)
'i eat 10 apples. so i was sick for 3 days.'
>>> "i eat {0} apples. so i was sick for {day} days.".format(10,day=3)
'i eat 10 apples. so i was sick for 3 days.'
>>> "{0:<10}".format("hi")
'hi        '
>>> "{0:>10}".format("hi")
'        hi'
>>> "{0:^10}".format("hi")
'    hi    '
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'
>>> y=3.265984756
>>> "{0:0.4f}".format(y)
'3.2660'
>>> "{0:10.4f}".format(y)
'    3.2660'
>>> "{{ eunwoo }}".format()
'{ eunwoo }'
>>> name='홍길동'
>>> age=50
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 50입니다.'
>>> f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.'
'나의 이름은 홍길동입니다. 나이는 51입니다.'
>>> d={'name':'홍길동','age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> f'{"hi":<10}'
'hi        '
>>> f'{"hi":>10}'
'        hi'
>>> f'{"hi":^10}'
'    hi    '
>>> f'{"hi":=^10}'
'====hi===='
>>> f'{"hi":!<10}'
'hi!!!!!!!!'
>>> y=3.235678745
>>> f'{y:0.4f}'
'3.2357'
>>> f'{y:10.4f}'
'    3.2357'
>>> f'{{eunwoo}}'
'{eunwoo}'
>>> "{0:!^12}".format("python")
'!!!python!!!'
>>> f'{"python":!^12}'
'!!!python!!!'
>>> a='eunwoo'
>>> a
'eunwoo'
>>> a.count('o')
2
>>> b='i want to go home'
>>> b.count('o')
3
>>> b.find('w')
2
>>> a.find('w')
3
>>> b.index('w')
2
>>> b.find('o')
8
>>> b.index('o')
8
>>> a.index('w')
3
>>> ",".join('eunwoo')
'e,u,n,w,o,o'
>>> ",".join(['a','b','c','d'])
'a,b,c,d'
>>> a
'eunwoo'
>>> a.upper()
'EUNWOO'
>>> c="SUNNY"
>>> c
'SUNNY'
>>> c.lower()
'sunny'
>>> a="    hi"
>>> a
'    hi'
>>> a.lstrip()
'hi'
>>> a="    hi    "
>>> a.rstrip()
'    hi'
>>> a.strip()
'hi'
>>> a.lstrip()
'hi    '
>>> a="life is too short"
>>> a
'life is too short'
>>> a.replace("life","your leg")
'your leg is too short'
>>> a
'life is too short'
>>> a.split()
['life', 'is', 'too', 'short']
>>> b="a/g/f/r/e"
>>> b
'a/g/f/r/e'
>>> b.split('/')
['a', 'g', 'f', 'r', 'e']
>>> odd=[1,3,5,7,9]
>>> odd
[1, 3, 5, 7, 9]
>>> a=[]
a
>>> 
>>> a
[]
>>> b=[1,2,3]
>>> b
[1, 2, 3]
>>> c=['life is too short']
>>> c
['life is too short']
>>> d=[1,2,'life','too']
>>> d
[1, 2, 'life', 'too']
>>> e=[1,2,'life',['is','too']]
>>> e
[1, 2, 'life', ['is', 'too']]
>>> b[0]
1
>>> b[1]
2
>>> b[2]
3
>>> b[0]+b[2]
4
>>> b[-1]
3
>>> e[-1]
['is', 'too']
>>> e[3][0]
'is'
>>> e[3][1]
'too'
>>> q=[1,2,['a','b',['life','too']]]
>>> q
[1, 2, ['a', 'b', ['life', 'too']]]
>>> q[2][2][0]
'life'
>>> b
[1, 2, 3]
>>> b=[1,2,3,4,5]
>>> b
[1, 2, 3, 4, 5]
>>> b[0:2]
[1, 2]
>>> a="12345"
>>> a
'12345'
>>> a[0:2]
'12'
>>> b[:2]
[1, 2]
>>> b[3:]
[4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> g=b[:2]
>>> t=b[3:]
>>> g
[1, 2]
>>> t
[4, 5]
>>> t[0]
4
>>> g[-1]
2
>>> A=[1,2,3,4,5]
>>> B=A[1:3]
>>> B
[2, 3]
>>> 