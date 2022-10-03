import random
random_num = random.randint(1,20)
#print("the secret number is: ", random_num)
guess = int(input('Enter a number: '))
while guess != random_num
  if (guess > random_num):
    print("Your guess is too high!!")
    guess = int(input('Input another number: '))
  if (guess < random_num):
    print("your guess is too low!!")
    guess = int(input('Input another number: '))
print("Correct!!")