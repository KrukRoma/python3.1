#1
a = int(input("Введіть перше число : "))
b = int(input("Введіть друге число : "))
for i in range(a,b+1):
    if i %7==0:
        print(i)

#2
c = int(input("Введіть перше число : "))
d = int(input("Введіть друге число : "))          
num = [n for n in range(c,d+1)]
print(num)
num1 = [g for g in range(c,d+1)]
print(num1[::-1])
for n in num:
    if n %7==0:
        print(n)
num2 = 0
for u in range(c,d+1):
    if u %5==0:
        num2 += 1
        print(num2)

#3
e = int(input("Введіть перше число : "))
f = int(input("Введіть друге число : "))
for num3 in range(e,f+1):
    if num3 %3==0 and num3 %5==0:
        print("FizzBuzz")
    elif num3 %3==0:
        print("Fizz")
    elif num3 %5==0:
        print("Buzz")
    else:
        print(num3)