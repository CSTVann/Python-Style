import random

#Allow user to input the lower number
lower = int(input('Enter the lower bound number:    '))
#Allow user to input the upper number
upper = int(input('Enter the upper bound number:    '))

#User to random the number between lower and upper
random_number = random.randint(lower, upper - 1)
print(random_number)

#Declare i=0 cuz in while loop i start from 0
i=0

#Loop if i not yet 7 stoll loop
while i !=7 :
    User_input = int(input("Enter your number {}:  ".format(i+1)))
    if User_input != random_number:
        if User_input > random_number:
            print('Your guess Higher than')
            i+=1#if this true loop one more time
        elif User_input < random_number:
            print('Your guess Smaller than')
            i+=1#if this true loop one more time
    elif User_input == random_number:
        print('You Win')
        break #break if this condition is true
if i == 7:#if the top condition false this conditions will true
    print('You Lose')