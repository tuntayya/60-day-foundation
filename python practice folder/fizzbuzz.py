for number in range(1,101):
    if number %3 ==0 and number % 5 ==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number% 5==0:
        print("Buzz")
    else:
        print(number)

numbers = [1,3,4,6,8,7,9,10]
total = 0
for number in numbers:
    total += number  

print(total)


word = "programming"
count = 0
for letter in word:
    if letter in "aeiou":
        count  +=1

print(count)

for x in range (1,6):
    for y in range(1,11):
        print (f"{x} * {y} = {x*y}")
