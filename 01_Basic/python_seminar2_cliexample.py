# command line interfaces CLIs

# Argparse: let us give inputs to the functions through terminal

# Example:

# python <fonk.ismi.py> --num1 <1st value> --num2 <2st value> --process <process type>
# python calculate-arg.py --num1 5 --num2 10 --process multiply

import argparse

def GetNamespace():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', type=str)

    parser.add_argument('-t', "--type", action="store", type=str)
    #default parameters if parameters are empty
    parser.set_defaults(type="all")

    return parser.parse_args()

def mean(numbers, choiceType=0):
    #choiceType = 1 --> even, = 2 --> odd, = 0 --> all
    total = 0
    n = 0
    if choiceType == 0: #all
        total = sum(numbers)
        n = len(numbers)
    elif choiceType == 1 or choiceType == 2: #even or odd
        for number in numbers:
            if not number % 2 and choiceType == 1:
                total += number
                n += 1
            elif number % 2 and choiceType == 2:
                total += number
                n += 1
    else:
        print('not supported')
    
    print(numbers)
    print(total/n)
    return total/n

# this py file can be run by command below via terminal
# python cliexample.py -l "1,2,3,4,5"
if __name__ == "__main__":
    namespace = GetNamespace()

    myList = [int(item) for item in namespace.list.split(',')]

    if namespace.type == "all":
        mean(myList)
    elif namespace.type == "even":
        mean(myList,1)
    elif namespace.type == "odd":
        mean(myList,2)