#1
num = int(input("Введіть число:"))
if num % 2 == 0:
    print("Парне")
#2
i = float(input("Введіть середній бал:"))
if i >= 90:
  print("Відмінник")
elif i >= 75:
  print("Молодець")
else:
  print("Старайся більше")
  #3
  for i in range(10, 101, 5):
  pdv = 1.2*i
  print("Ціна без ПДВ:", i, "Ціна з ПДВ:", pdv)
  #4
  a = int(input("Введіть число:"))
b = int(input("Введіть число:"))
c = int(input("Введіть число:"))
if a > b and a > c:
  print("a")
elif a < b and b > c:
  print("b")
elif c > a and c > b:
  print("c")
  #5
  x = 1000
a = 1
while x <= 5000:
  print(f"місяць {a}:", x)
  a += 1 
  x += 300
  #6
  a = int(input("Введіть рік:"))
if a % 4 == 0 and not (a % 100 == 0 or a % 400 == 0):
  print("Високосний")
else:
  print("Звичайний рік")
  #7
  for i in range(1,21):
  if i % 4 == 0:
    continue
  print(i)
  #8
  x = 10000
b = 1
while x > 0:
  print(f"місяць {b}", x)
  x = (x - 1200)*1.02
  b += 1
  #extra
  a = 0
b = 0
while True:
  a = float(input("Ввeдіть ваш місячний дохід або 0 для виходу:", ))  
  if a == 0:
    break
  elif a < 0:
    print("Дохід не може бути від'ємним")
    continue
  else:
    b += a
    print("Ваш дохід збережино", b) 