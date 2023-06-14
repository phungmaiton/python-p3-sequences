#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []

    if length == 0:
        print(fibonacci_list)
    elif length == 1:
        fibonacci_list.append(0)
        print(fibonacci_list)
    elif length > 1:
        fibonacci_list = [0, 1]

        while len(fibonacci_list) < length:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        
        print(fibonacci_list)
    