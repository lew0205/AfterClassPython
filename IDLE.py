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
>>> s=[1,2,3,['a','b','c'],4,5]
>>> s
[1, 2, 3, ['a', 'b', 'c'], 4, 5]
>>> a[2:5]
'345'
>>> s[3:5]
[['a', 'b', 'c'], 4]
>>> s[3][:2]
['a', 'b']
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> 'abc'+'def'
'abcdef'
>>> a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> len(a)
3
>>> len(s)
6
>>> a[2]+"hi"
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    a[2]+"hi"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a[2])+"hi"
'3hi'
>>> a
[1, 2, 3]
>>> a[2]=4
>>> a
[1, 2, 4]
>>> del a[2]
>>> a
[1, 2]
>>> a=[1,2,3,4,5,6,7]
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> del a[2:]
>>> a
[1, 2]
>>> a=[1,2,3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append("hi")
>>> a
[1, 2, 3, 4, 'hi']
>>> a.append([5,6])
>>> a
[1, 2, 3, 4, 'hi', [5, 6]]
>>> b=[5,6,9,8,4,5,1,2]
>>> b.sort()
>>> b
[1, 2, 4, 5, 5, 6, 8, 9]
>>> d=['g','h','t','a']
>>> d
['g', 'h', 't', 'a']
>>> d.sort()
>>> d
['a', 'g', 'h', 't']
>>> b
[1, 2, 4, 5, 5, 6, 8, 9]
>>> b.reverse()
>>> b
[9, 8, 6, 5, 5, 4, 2, 1]
>>> d=['b','c','a']
>>> d
['b', 'c', 'a']
>>> d.reverse()
>>> d
['a', 'c', 'b']
>>> d.sort()
>>> d
['a', 'b', 'c']
>>> b
[9, 8, 6, 5, 5, 4, 2, 1]
>>> b.index(4)
5
>>> b.index(5)
3
>>> b.index(3)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    b.index(3)
ValueError: 3 is not in list
>>> d
['a', 'b', 'c']
>>> d.append('e')
>>> d
['a', 'b', 'c', 'e']
>>> d.insert(3,'d')
>>> d
['a', 'b', 'c', 'd', 'e']
>>> d.remove('b')
>>> d
['a', 'c', 'd', 'e']
>>> d.append('e')
>>> d.append('t')
>>> d.append('e')
>>> d
['a', 'c', 'd', 'e', 'e', 't', 'e']
>>> d.remove('e')
>>> d
['a', 'c', 'd', 'e', 't', 'e']
>>> d.remove('e')
>>> d
['a', 'c', 'd', 't', 'e']
>>> a
[1, 2, 3, 4, 'hi', [5, 6]]
>>> a.pop()
[5, 6]
>>> a
[1, 2, 3, 4, 'hi']
>>> s
[1, 2, 3, ['a', 'b', 'c'], 4, 5]
>>> t=[1,2,3,4,4,5,6,6]
>>> t
[1, 2, 3, 4, 4, 5, 6, 6]
>>> t.count(4)
2
>>> t.extend([8,9])
>>> t
[1, 2, 3, 4, 4, 5, 6, 6, 8, 9]
>>> t.extend(8)
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    t.extend(8)
TypeError: 'int' object is not iterable

Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1=()
>>> t1
()
>>> t2=(1)
>>> t2
1
>>> t3=(1,3,5)
>>> t3
(1, 3, 5)
>>> t4=('a','b',('ab','cd'))
>>> t4
('a', 'b', ('ab', 'cd'))
>>> t5=5,6,7
>>> t5
(5, 6, 7)
>>> t1=(1,2,'a','b')
>>> t1
(1, 2, 'a', 'b')
>>> del t1[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> t1[2]=34
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t1[2]=34
TypeError: 'tuple' object does not support item assignment
>>> t1[0]
1
>>> t1[3]
'b'
>>> t1[1:]
(2, 'a', 'b')
>>> t2=3,4,5,6
>>> t1+t2
(1, 2, 'a', 'b', 3, 4, 5, 6)
>>> t2*3
(3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6)
>>> len(t1)
4
>>> len(t2)
4
>>> dic = {'name':'eunwoo', 'birth':'0205', 'hobby':'game'}
>>> dic
{'name': 'eunwoo', 'birth': '0205', 'hobby': 'game'}
>>> dic2={1:'Life', 2:'is', 3:'too', 4:'short'}
>>> dic2
{1: 'Life', 2: 'is', 3: 'too', 4: 'short'}
>>> dic3={1:[1,2,3]}
>>> dic3
{1: [1, 2, 3]}
>>> dic2[5]='python'
>>> dic2
{1: 'Life', 2: 'is', 3: 'too', 4: 'short', 5: 'python'}
>>> del dic2[3]
>>> dic2
{1: 'Life', 2: 'is', 4: 'short', 5: 'python'}
>>> dic['name']
'eunwoo'
>>> a={1:'a', 1:'python'}
>>> a
{1: 'python'}
>>> a[1]='b'
>>> a
{1: 'b'}
>>> a[[1,2]]='b'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[[1,2]]='b'
TypeError: unhashable type: 'list'
>>> a={1,2:'b'}
SyntaxError: invalid syntax
>>> a
{1: 'b'}
>>> dic.keys()
dict_keys(['name', 'birth', 'hobby'])
>>> for k in a.keys():
	print(k)

	
1
>>> 
>>> 
>>> 
>>> for k in dic.keys():
		print(k)

		
name
birth
hobby
>>> list(dic.keys())
['name', 'birth', 'hobby']
>>> dic.values()
dict_values(['eunwoo', '0205', 'game'])
>>> dic.items()
dict_items([('name', 'eunwoo'), ('birth', '0205'), ('hobby', 'game')])
>>> list(dic.items())
[('name', 'eunwoo'), ('birth', '0205'), ('hobby', 'game')]
>>> dic.clear()
>>> dic
{}
>>> a
{1: 'b'}
>>> a[(1,2)]='a'
>>> a
{1: 'b', (1, 2): 'a'}
>>> a.get(1)
'b'
>>> a.get((1,2))
'a'
>>> a.get(3)
>>> None
>>> t1=(1,2)
>>> t1
(1, 2)
>>> s1=set([1,2,3])
>>> s1
{1, 2, 3}
>>> s2=set("python")
>>> s2
{'o', 'p', 'y', 'h', 'n', 't'}
>>> s3=set("life is too")
>>> s3
{'o', 'i', 'f', ' ', 's', 'l', 'e', 't'}
>>> s1
{1, 2, 3}
>>> l1=list(s1)
>>> l1
[1, 2, 3]
>>> l1[0]
1
>>> t1=tuple(s1)
>>> t1
(1, 2, 3)
>>> t1[0]
1
>>> s1=set([1,2,3,4,5,6])
>>> s2=set([3,4,5,6,7,8])
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s2
{3, 4, 5, 6, 7, 8}
>>> s1&s2
{3, 4, 5, 6}
>>> s1-s2
{1, 2}
>>> s2-s1
{8, 7}
>>> s1.intersection(s2)
{3, 4, 5, 6}
>>> s1+s2
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s1+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1|s2
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s1.difference(s2)
{1, 2}
>>> s1.add(9)
>>> s1
{1, 2, 3, 4, 5, 6, 9}
>>> s1.add(3)
>>> s1
{1, 2, 3, 4, 5, 6, 9}
>>> s1.update([7,6,4,0])
>>> s1
{0, 1, 2, 3, 4, 5, 6, 7, 9}
>>> s1.remove(0)
>>> s1
{1, 2, 3, 4, 5, 6, 7, 9}
>>> kor=80
>>> mat=75
>>> eng=55
>>> sum=kor+mat+eng
>>> sum
210
>>> if(13%2==0){print("짝수")}else{print("홀수")}
SyntaxError: invalid syntax
>>> if(13%2==0){print("짝수")}else{print("홀수")}
SyntaxError: invalid syntax
>>> if(13%2==0){print("짝수")}else{print("홀수")}
SyntaxError: invalid syntax
>>> if(13%2==0)
SyntaxError: invalid syntax
>>> if(13%2==0):print("짝수")else:print("홀수")
SyntaxError: invalid syntax
>>> num=["881120-1068324"]
>>> num[:7]
['881120-1068324']
>>> num=881120-1068324
>>> num
-187204
>>> num=[8,8,1,1,2,0,-,1,0,6,8,3,2,4]
SyntaxError: invalid syntax
>>> num=[8,8,1,1,2,0,'-',1,0,6,8,3,2,4]
>>> num
[8, 8, 1, 1, 2, 0, '-', 1, 0, 6, 8, 3, 2, 4]
>>> num[:6]
[8, 8, 1, 1, 2, 0]
>>> num[7:]
[1, 0, 6, 8, 3, 2, 4]
>>> pin=”881120-1068324”
SyntaxError: invalid character '”' (U+201D)
>>> pin="881120-1068324"
>>> pin
'881120-1068324'
>>> yymmdd="19"+pin[:6]
>>> num=pin[7:]
>>> print(yymmdd)
19881120
>>> print(pin)
881120-1068324
>>> pin="881120-1068324"
>>> yymmdd="19"+pin[:6]
>>> pin=num[7:]
>>> print(yymmdd)
19881120
>>> print(pin)

>>> pin
''
>>> pin=num[7:]
>>> pin
''
>>> pin="num[7:]
SyntaxError: EOL while scanning string literal
>>> pin="num[7:]"
>>> pin
'num[7:]'
>>> pin="881120-1068324"
>>> yymmdd="19"+pin[:6]
>>> num=pin[7:]
>>> print(yymmdd)
19881120
>>> print(num)
1068324
>>> str='a:b:c:D'
>>> str.replace(':','#',3)
'a#b#c#D'
>>> li=[1,3,4,5,2]
>>> li.resort()
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    li.resort()
AttributeError: 'list' object has no attribute 'resort'
>>> li.unsort()
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    li.unsort()
AttributeError: 'list' object has no attribute 'unsort'
>>> li.sort()
>>> li.reverse
<built-in method reverse of list object at 0x000001704B6AE0C0>
>>> li.reverse()
>>> li
[5, 4, 3, 2, 1]
>>> li=[1,3,4,5,2]
>>> li.sort()
>>> li.reverse
<built-in method reverse of list object at 0x000001704B64D440>
>>> li=[1,3,4,5,2]
>>> li.sort()
>>> li.reverse()
>>> li
[5, 4, 3, 2, 1]
>>> li=['Life','is','too','short']
>>> result=li[0]+ li[1]+ li[2]+ li[3]
>>> print(result)
Lifeistooshort
>>> li.split(',')
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    li.split(',')
AttributeError: 'list' object has no attribute 'split'
>>> li
['Life', 'is', 'too', 'short']
>>> li=['Life','is','too','short']
>>> result=li[0]+ +li[1]+ +li[2]+ +li[3]
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    result=li[0]+ +li[1]+ +li[2]+ +li[3]
TypeError: bad operand type for unary +: 'str'
>>> li=['Life','is','too','short']
>>> result=li[0]+' '+li[1]+' '+li[2]+' '+li[3]
>>> print(result)
Life is too short
>>> tu=1,2,3
>>> tu.add(4)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    tu.add(4)
AttributeError: 'tuple' object has no attribute 'add'
>>> t1=1,2,3
>>> t1+4
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    t1+4
TypeError: can only concatenate tuple (not "int") to tuple
>>> t1=1,2,3
>>> t1+(4)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    t1+(4)
TypeError: can only concatenate tuple (not "int") to tuple
>>> t1=1,2,3
>>> t1=t1+(4)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    t1=t1+(4)
TypeError: can only concatenate tuple (not "int") to tuple
>>> t1=t1+(4,)
>>> t1
(1, 2, 3, 4)
>>> t1=1,2,3
>>> t1=t1+4,
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    t1=t1+4,
TypeError: can only concatenate tuple (not "int") to tuple
>>> t1=1,2,3
>>> t1=t1+(4,)
>>> print(t1)
(1, 2, 3, 4)
>>> a=dict()
>>> a
{}
>>> a['name']='python'
>>> a[('a'.,)='python'
  
SyntaxError: invalid syntax
>>> a[('a',)='python'
  
SyntaxError: invalid syntax
>>> a[[1]] = ‘python’

SyntaxError: invalid character '‘' (U+2018)
>>> a[[1]] = 'python'
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    a[[1]] = 'python'
TypeError: unhashable type: 'list'
>>> a[250] = 'python'
>>> a
{'name': 'python', 250: 'python'}
>>> a[('a',)]='python'
>>> a
{'name': 'python', 250: 'python', ('a',): 'python'}
>>> a[[1]]='python'
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    a[[1]]='python'
TypeError: unhashable type: 'list'
>>> a=[1,1,1,1,2,2,3,3,4,5,6,7,8]

>>> aSet=a
>>> b=aSet
>>> print(b)
[1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> aSet
[1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> a=[1,1,1,1,2,2,3,3,4,5,6,7,8]
>>> aSet=set(a)
>>> b=aSet
>>> print(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> money=True
>>> if money:
		print("taxi")

		
taxi
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
Taxi
>>> x=3
>>> y=2
>>> x>y
True
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
True
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py", line 2, in <module>
    card=false
NameError: name 'false' is not defined
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
Taxi
>>> 1 !in [1,2,3]
SyntaxError: invalid syntax
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
Walk
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
걸어가세연
>>> pocket=[wallet=['money','card'],'phone','Buds']

SyntaxError: invalid syntax
>>> 
======================================================================================== RESTART: C:/Users/user/Desktop/잉/공부/코딩/python/방학방과후/if.py ========================================================================================
걸어다니는 풀은? 뚜벅초 ㅋㅋㅋㅋㅋㅋ
>>> 