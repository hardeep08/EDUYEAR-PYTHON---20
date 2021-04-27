
by = int(input("Enter your birth year"))
age = 2021 - by
print("your age is ", age)

a = int(input("Enter the First Number"))
b = int(input("Enter the Second Number"))

c = a+b
d = a-b
e = a*b
f = a/b
g = a//b
h = a%b
i = a**b

print("Addition of 2 numbers is = ", c)
print("Subtraction of 2 numbers is = ", d)
print("Multiplication of 2 numbers is = ", e)
print("Decimal Division of 2 numbers is = ", f)
print("Floor Division of 2 numbers is = ", g)
print("Remainder of 2 numbers is = ", h)
print("Power of 2 numbers is = ", i)



str = input()
print(str.count('y'))

for i in range(len(str)):
    if i % 2 == 0:
        print(str[i])