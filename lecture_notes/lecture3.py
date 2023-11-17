var1 = 'a'
var2 = 'a'
var3 = 'a'
var4 = 'a'

var1 = ['a']
var2 = ['a']
var3 = ['a']
var4 = ['a']

lst1 = ['a']
lst2 = ['b', lst1]
lst3 = ['b', ['a']]

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')
lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}")

print(f"This is lst1 after modifying lst2: {lst1}")

happy = True
if happy is True:
 print("I am happy")
print("This will print regardless of the value of happy")

happy = 1
if happy:
    print("I am happy")


happy = 0.0
if happy:
    print("I am happy")


var1 = 'a'
var2 = 'a'
print(var1 is var2)
print(var1 == var2)


workinghours = input("enter number of hours you worked this week:")
workinghours = int(workinghours)
if workinghours > 35:
    weeklypay = (workinghours-35) * 88.9 + 51.45 * 35
else:
    weeklypay = workinghours * 51.45

print(weeklypay)



d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key in d:
    print(key)


d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for val in d.values():
    print(val)




numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
temp_largest = numbers [0]
print ('Before', temp_largest)
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print (number, temp_largest)
print (f'The largest value is {temp_largest}')


years = [2018, 2019, 2020]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    ]

for year in years:
   for month in months:
       print("Year: {}, Month: {}".format(year, month))


A=[1,2,3]
B="1,2,3"
for A in A:
    for B in B:
        print(" {}, {}".format(A, B))


for i in range(1,4):
    for j in range(1,4):
        if i<=j:
            print(i,j)

for even in range(0, 10, 2):
    if even > 2:
        continue

print(even)

for even in range(0,10,2):
    if even>2:
        break

print(even)

for add in range(1,10,2):
    for even in range(0, 10, 2):
        if even > 2:
            break

print(even,add)

for add in range(1,10,2):
    for even in range(0, 10, 2):
        if even > 2:
           continue

print(even,add)
