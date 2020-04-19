import random

print('I made up a number. Can you guess it?\n')
number = random.randint(1, 100)

while True:
    user_num = int(input())
    if user_num > number:
        print('Too high')
        continue
    elif user_num < number:
        print('Too low')
        continue
    else:
        print('You won!')
        break
print('The number was ' + str(number))