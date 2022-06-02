from random import randint
import sys

def check_answer(guessed_number, number):
    if guessed_number == number:
        print('Congrats you guessed the number')
        return True
    else:
        print('Please try again.')
    pass

def guess_func(a, b):    
    number = randint(a, b)

    print(f'Guessing a number between {a} and {b}')

    counter = 0

    while True:
        if counter == 5:
            print('Game Over')
            break
        try:
            guessed_number = int(input('Enter a number to guess: '))
            if(check_answer(guessed_number, number)):
                break
        except ValueError:
            print('Please enter valid number2')
            continue
        finally:            
            counter += 1


try:

    if len(sys.argv) != 1:
        start = int(sys.argv[1])
        end = int(sys.argv[2]) 
        guess_func(start, end)

except ValueError:
    print('Please enter valid number')


