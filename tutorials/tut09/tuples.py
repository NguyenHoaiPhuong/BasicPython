def tuple_define():
    tup1 = ('physics', 'maths', 40, 50)
    print('tup1 = ', tup1)

def tuple_access_value():
    tup = (1, 2, 3, 4, 5, 6, 7)
    print('tup = ', tup)
    print('tup[1] = ', tup[1])
    print('tup[1:5] = ', tup[1:5])

def tuple_update():
    tup = (1, 2, 3, 4, 5, 6, 7)
    print('Original tuple:', tup)

    try:
        tup[0] = 10
    except Exception as e:
        print('Assignment tup[0] = 10:', e)

    tup = (10, 2, 3, 4, 5, 6, 7)
    print('Updated tuple:', tup)

def tuple_delete():
    tup = (1, 2, 3, 4, 5, 6, 7)
    print('Original tuple:', tup)

    try:
        del tup[2]
    except Exception as e:
        print("del tup[2]:", e)
        print("Conclusion: Removing individual tuple elements is not possible")

    del tup
    try:
        print('After removing the whole tuple:', tup)
    except Exception as e:
        print(e)

def tuple_concatenate():
    tup1 = (1, 2, 3)
    tup2 = (4, 5, 6, 7)
    print("tup1 =", tup1)
    print("tup2 =", tup2)

    tup = tup1 + tup2
    print("tup = tup1 + tup2 =", tup)

def tuple_repeat():
    tup = ('Hi',)
    print("Original tuple:", tup)

    tup *= 4
    print("After repeating 4 times:", tup)

def tuple_membership():
    tup = (1, 2, 3)
    print("Original tuple:", tup)

    for x in tup:
        print(x)