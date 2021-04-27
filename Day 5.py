List = [10, 21, 121 , 121 , 21, 10]
print(List)

even_count, odd_count = 0 , 0
for i in List:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

minimum = maximum = List[0]
for i in List[1:]:
    if i < minimum:
        minimum = i
    else:
        if i > maximum :
            maximum = i
print(minimum, maximum)

if List == List[::-1]:
    print("List is palindrome")
else:
    print("List is not palindrome")

for num in List:
    num = str(num)
    if num == num[::-1]:
        print(num)
