def access_value_in_string():
    var = 'Hello World'
    print('String:', var)

    for i in range(len(var)):
        str_res = 'Letter with index ' + str(i) + ' in string: ' \
        + var[i]
        print(str_res)

    print('Slicing string from index 0 to 4:', var[:5])

def update_string():
    var = 'Hello World'
    print('Original string:', var)

    var = var[:5] + ' python'
    print('Updated string:', var)

def format_string():
    var = 'My name is %s and I am %d years old' % ('Nguyen Hoai Phuong', 33)
    print(var)

def string_built_in_funcs():
    origin_string = 'hello world'
    print('Original string:', origin_string)

    capitalized_string = origin_string.capitalize()
    print('Capitalized:', capitalized_string)

    uppercase_string = origin_string.upper()
    print('Uppercase string:', uppercase_string)

    lowercase_string = uppercase_string.lower()
    print('Lowercase string:', lowercase_string)

    replace_string = lowercase_string.replace('world', 'python')
    print('Replaced string:', replace_string)

    list_string = replace_string.split()
    print('String after split:')
    for i in range(len(list_string)):
        print(list_string[i])