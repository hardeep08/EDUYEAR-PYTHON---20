#Ques1
n = int(input("Enter the starting point"))
m = int(input("Enter the ending point"))
for i in range(n , m):
    if(i%5==0 and i%7==0):
      print(i)

#Ques 2
s = ''
p = 0
i = int(input('Enter no. of terms :'))
for i in range(i):
    s = s + str('2')
    p = int(s) + p

print(p)

#Ques3
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n :
    fact = fact*i
    i = i+1
print("Factorial of {} is {}".format(n, fact))


#Ques4
summ = 0
while True:
    value = input("Enter a number or press q to quit:")
    if value == 'q':
        break
    summ = int(summ) + int(value)

print(summ)