'arithemetic'
sum = "hello" + "dbhfbvh"
print(sum)


'relational operator'

s=10>20
print(s)
s=10<20
print(s)

'ASSIGN'
a = 10
b = 20
a+=10
b-=1
print(a)
print(b)

'logical operator'

a=True
b=False
c=True
print(a and b and c)
print( c and a)
print(5 and 6)
print(not a)
print(not b)
a= 10>30,56>12
b= 56<89,101<555
print(a)
print(b)
'mu examples'
num=10
nums=50
sum=num+nums
print('the sum  is :{2}'.format(num,nums,sum))



count = 1
width = 20
for i in range(6):
    print(("@"*count).center(width))
    count +=2
print("||".center(width))


x=10
y=20
temp=x
x=y
y=temp
print(x, y)
print(y , x)


a=200
b=201
print(a == b)


a=200
b=200
a=a+1
b=b+12
print(a is b)


a=200
b=201
print(a is not b)


'membership opertor'

string1 = "@jfngrwehgikrsbvkjhbrkjvbkjrebkj@"
print("@" in string1)


'precedence'
a = (10 + 2 * 5 / 8 - 10 <= 1.25 and 10<2 )
print(a)