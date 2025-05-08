#1
name = "Angelina"
age = 18
number = 3.8
surname = "Popova"
sm = True
ms = False
num = 23
vagon = "6"
misce = "65"
Today = False
print(name)
#2
a = 1
b = 2
c = a
a = b
b = c
print(a)
print (b)
#3
x = 3
y = 9
print(2*x+3*y)
print(x**2+2*x*y+y**2)
print(2/8*x-13/7*y)
print(y**(4*x-2*y)**0.5)
print(x%y)
print((y//x)**2)
print(x>y)
print((x**2)!=y)
#4
name = "bread"
price = 20
side = name
name = price 
print(name)
#5
x1=2
x2=4
x3=32
x4=12
y = ((x1>x3) or (x2>x4) and (not(x2!=x3)) or(x1==x4))
print(y)
#6
height = int(input("Введіть ваш зріс, м:"))
weight = int(input("Введіть вашу вагу, кг:"))
bmi = weight/height**2
print(f"При вазі {weight} кг і рості {height} м, Ваш ВМІ складає {bmi}")
#додаткове
r1 = 30
S1 = 3.14*r1**2
print(S1)
r2 = 36.3
S2 = 3.14*r2**2
print(S2)
diff = ((S2-S1)/S1)*100
print(f"Друга піца на {diff:.2f}% більша за першу")