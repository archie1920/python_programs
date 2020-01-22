#FizzBuss program
#number divided by 3 - print Fizz
#number divided by 5 - print Buzz
#else print the number

fiz = 'Fizz'
buz = 'Buzz'

for i in range(1, 100):
    if i % 15 == 0:
        print(fiz+buz, end=",")
    elif i % 3 == 0:
        print(fiz, end=",")
    elif i % 5 == 0:
        print(buz, end=",")
    else:
        print(i, end=",")

