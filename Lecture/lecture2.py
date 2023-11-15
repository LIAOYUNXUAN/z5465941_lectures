
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')


string1 = "Monty Python's Flying Circus"
string2 = 'I like the "Dead Parrot" sketch'
string3 = '''When Cleese says: 
"Now that's what I call a dead parrot" '''

i = 1
test = i == 1
print(test)

f = 1 / 2.0000000000000000000001
test = f == 1 / 2
print(test)

1 < 2
2 < 2
2 <= 2
1 > 2
2 > 2
1 == 2
2 == 2


not True
not False
True and True
True and False
False and True
False and False
True or True
True or False
False or True


y = type(1)
print(y)
i = 1
type(i)
f = 1.0
type(f)


x = 1
print(type(x))
xstr = '1'
print(type(xstr))
test = x == xstr
print(test)
print(type(test))

2 + None
'3' + 2
print('3' + '2')
print('x' * 2)

import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')

df = yfinance.download(tic, start, end)

x = 1
print(x)

x = 'abc'
x = str('abc')
#upper(x)

x = str('abc')
xup = str.upper(x)
print(xup)

x = str.upper('abc')
print(x)
y = 'abc'.upper()
print(y)

str.upper
'abs'.upper

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_upper = weird_case.upper()

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_lower = weird_case.lower()

"Hi".center(40)
"Hi".center(40, '-')

a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}")

import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')


str = 'this is a string'

x = str(5)
print(x)

_var = 1
print(_var)

length=56
width=33
height=30.5
volume=length*width*height
print(f"the volume of the box is {volume}cubic centimeters")

line='From nickname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain=line.split()[1].split('@')[1]
print(domain)

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.copy()
dic1.update({'a': 0, 'd': 4})
print(dic1)


list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.remove('bad')
sol.insert(10,'including')
sol.insert(3,'good')
sol = sol + list_b


