def append_list(mylist):
    mylist.append([1, 2, 3, 4])

def change_list(mylist):
    mylist = [1, 2, 3, 4]

def pass_by_value():
    pass

def pass_by_ref():
    mylist = [10, 20, 30]
    append_list(mylist)
    print(mylist)