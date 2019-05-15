import math
import random
import numpy as np
import matplotlib.pyplot as plt

def number_types():
    int_num = 10
    print('int_num = ', int_num, '. Type of int_num:', type(int_num))

    float_num = 1234.567
    print('float_num = ', float_num, '. Type of float_num:', type(float_num))

    complex_num = 123 + 456j
    print('complex_num = ', complex_num, '. Type of complex_num:', type(complex_num))

def number_type_conversion():
    int_num = 10
    print('int_num = ', int_num, '. Type of int_num:', type(int_num))

    float_num = float(int_num)
    print('float_num = ', float_num, '. Type of float_num:', type(float_num))

    complex_num = complex(int_num, float_num)
    print('complex_num = ', complex_num, '. Type of complex_num:', type(complex_num))

def math_funcs():    
    x = -10
    y = 10.12543
    z = 1

    print('x = ', x, ', y = ', y)

    print('abs(x) = ', abs(x))
    print('fabs(x) = ', math.fabs(x))   # Float absolute
    print('ceil(y) = ', math.ceil(y))
    print('floor(y) = ', math.floor(y))
    print('round(y, 2) = ', round(y, 2))
    print('exp(z) = ', math.exp(z))
    print('log(y) = ', math.log(y))
    print('log10(y) = ', math.log10(y))
    print('sqrt(y) = ', math.sqrt(y))
    print('pow(y, x) = ', math.pow(y, x))

def math_funcs_plot():
    x = np.linspace(0.0, 10.0, 1000)
    # x = np.append(x, np.linspace(2.0, 100.0, 99), axis=None)

    y1 = x
    plt.plot(x, y1,'r--', label='y = x')
    
    y2 = np.power(x, 2)
    plt.plot(x, y2,'b--', label='y = x^2')

    y_log = np.log(x)
    plt.plot(x, y_log,'g--', label='y = log(x)')

    y_xlog = x*np.log(x)
    plt.plot(x, y_xlog,'ro', label='y = x*log(x)')

    plt.axis([0, 10, -5, 100])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def trigonometric_funcs_plot():
    x = np.linspace(0, 2*math.pi, 100)

    y_sin = np.sin(x)
    plt.plot(x, y_sin, 'ro', label='sin')

    y_cos = np.cos(x)
    plt.plot(x, y_cos, 'bs', label='cos')

    y_tan = np.tan(x)
    plt.plot(x, y_tan, 'g--', label='tan')
    
    plt.axis([0, 2*math.pi, -10, 10])
    plt.title("Trigonometric functions")
    plt.xlabel("x (rad)")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def random_number_funcs():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List of numbers:", numbers)
    for _ in range(len(numbers)):
        print(random.choice(numbers))
    
    letters = 'python'
    print("Letters:", letters)
    for _ in letters:
        print(random.choice(letters))