import pandas as pd 
import numpy as np 

def test_func(a):
    return f'You have entered {a} as name'

if __name__ == '__main__':
    a = input("Enter your first name :")
    b = input("Enter your surname :")
    
    
    print(a + b)

    print(test_func(a))