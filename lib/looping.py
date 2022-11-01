#!/usr/bin/env python3

# LIST COMPREHENSION
# allow us to transform sequences of data in 1 line :0
# keep in mind when decinding between looping and list comprehensions
#   1. should only be used for iterable objects such as list or set
#   2. can be difficult to read in 1 line

# from this:
# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)
# to:
# inch_heights = [height * 7920 for height in player_heights]


def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # squared_list = []
    # for num in int_list:
    #     squared_int = num ** 2
    #     squared_list.append(squared_int)
    # return squared_list

    # solution with list comprehension
    return [num ** 2 for num in int_list]


def fizzbuzz():
    for i in range(100):
        num = i + 1
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
