num = int(input('What number would you like to go up to: '))

for i in range (1, num):
    if i % 15 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)