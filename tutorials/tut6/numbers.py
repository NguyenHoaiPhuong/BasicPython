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
    y = 10.1

    print('x = ', x, ', y = ', y)

    print('abs(x) = ', abs(x))
