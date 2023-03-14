from traceback import print_tb


print(1 +5)

a = 88
b = 103
print(a + b)

c = -36
d = 25
print(c + d)

e = 5.5
f = 2.5
print(e + f)

g = 75.67
h = 32
print(g - h)

i = 3.3
print(+i)

j = -19
print(+j)

print(-i)
print(-j)

k = 100.1
l = 10.1
print(k * l)

m = 80
n = 5
print(m / n)

o = 85
p =15
print(o % p)

q = 36.0 
r = 6.0
print(q % r)

s = 52.25
t = 7
print(s ** t)

u = (10 + 10) * 5
print(u)

w = 5
w += 1
print(w)

for x in range (0, 7):
    x *= 2
    print(x)

a=3
b=4
c=1
d=5
e=3
f=a+b-c*d+e/d
g=a+b-c*(d+e)/d
h=a+(b-c)*d+e/d
i=(a+b-c)*d+e/d
print(f,g,h,i)

v=2
w=3
x=4
y=19
z=23
a=v**v//x%x+y%w*z//x
b=v**(v//x)%x+y%(w*z)//x
print(a,b)

a = True
print(a)
print(type(a))
b = False 
print(b)
print(type(b))

a=2
b=3
print(a==b)
print(a!=b)
print(a>=b)
print(a>=a)
print(a<=a)
print(a>b)
print(a < b) 

a=2
b=5
a=b
print(a)
a=2
b=5
print(a==b)

x=3
y=4
z=5
print(x<y and y<z)
print(x==y or y==z)
print(not z <=y)

x = 4
y = 1
z = 7
print(x <= y and (not y <z))
print(z != x and (x > 2 or y > 2))
print(not (x <z or y >= z))

x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)

Sammy = 'Sammy'
sammy = 'sammy'
also_Sammy = 'Sammy'

print('Sammy == sammy:', Sammy == sammy)
print('Sammy == also_Sammy', Sammy == also_Sammy)

print((9 > 7) and (2 < 4))
print((8 == 8) or (6 != 6))
print(not(3 <=1))

print((-0.2 > 1.4) and (0.8 < 3.1)) # One original expression is False
print((7.5 == 8.9) or (9.2 != 9.2)) # Both original expressions are False       
print(not(-5.7 <= 0.3))             # The original expression is True

grade = 83
if grade >= 65:
    print('Passing grade')
else:
    print('Failing grade')
