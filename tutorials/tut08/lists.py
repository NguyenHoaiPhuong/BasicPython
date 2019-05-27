def list_define():
    List = ["Akagi", 1986, "Yushin", 1991]
    print(List)
    print("First Element:", List[0])
    print("Last Element:", List[-1])
    print("Length of the list:", len(List))

def list_update():
    List = ["Akagi", 1985, "Yushin", 1991]
    print("Original list:", List)
    print("Original list address:", hex(id(List)))
    print("Original list elements' addresses:", hex(id(List[0])), hex(id(List[1])), hex(id(List[2])), hex(id(List[3])))   
    
    List[1] = 1986
    print("New list:", List)
    print("New list address:", hex(id(List)))
    print("New list elements' addresses:", hex(id(List[0])), hex(id(List[1])), hex(id(List[2])), hex(id(List[3])))

def list_delete():
    List = ["Akagi", 1985, "Yushin", 1991]
    print("Original:", List)
    print("Original list address:", hex(id(List)))
    delIdx = 2
    del(List[delIdx])
    print("After deleting element", delIdx, ":", List)
    print("New list address:", hex(id(List)))

def list_concatenate():
    list1 = [1, 2, 3]
    print("list1:", list1)
    print("list1 address:", hex(id(list1)))
    print( "list1 elements' addresses:", hex(id(list1[0])), hex(id(list1[1])), hex(id(list1[2])) )
    
    list2 = [4, 5]
    print("list2:", list2)
    print("list2 address:", hex(id(list2)))
    print( "list2 elements' addresses:", hex(id(list2[0])), hex(id(list2[1])) )
    
    list3 = list1 + list2
    print("list3 = list1 + list2 =", list3)
    print("list3 address:", hex(id(list3)))
    print( "list3 elements' addresses:", hex(id(list3[0])), hex(id(list3[1])), hex(id(list3[2])), \
            hex(id(list3[3])), hex(id(list3[4])) )

def list_append():
    list_origin = [1, 2]
    print("Origin List:", list_origin)
    print( "Origin List elements' addresses:", hex(id(list_origin[0])), hex(id(list_origin[1])) )
    
    list_origin.append(3)
    print("After appending:", list_origin)
    print( "List elements' addresses:", hex(id(list_origin[0])), hex(id(list_origin[1])), hex(id(list_origin[1])) )

    seq = [4, 5, 6]
    list_origin.extend(seq)
    print("After extending:", list_origin)

def list_insert():
    list_origin = [1, 2]
    print("Origin List:", list_origin)
    print( "Origin List elements' addresses:", hex(id(list_origin[0])), hex(id(list_origin[1])) )
    
    list_origin.insert(2, "Akagi")
    list_origin.insert(0, "Yushin")
    print( "After inserting new elements:", list_origin )
    print( "Elements' addresses:", hex(id(list_origin[0])), hex(id(list_origin[1])), \
            hex(id(list_origin[2])), hex(id(list_origin[3])) )

def list_remove():
    list_origin = [1, 2, 3, 4]
    print("Origin List:", list_origin)

    i = 2
    list_origin.remove(i)
    print("After removing", i, ":", list_origin)

    i = 5
    try:        
        list_origin.remove(i)
        print("After removing", i, ":", list_origin)
    except ValueError:
        print(i, "is not in the list")    
   
def list_repeat():
    list_origin = [1, 'Hi']
    print("Origin List:", list_origin)

    list_origin *= 4
    print("After repeating 4 times:", list_origin)

def list_slice():
    list_origin = [1, 2, 3, 4, 5, 6]
    print("Origin List:", list_origin)

    list_new = list_origin[1:4]
    print("Slice from 1 to 4:", list_new)

def list_built_in_funcs():
    list_origin = [1, 2, 2, 4, 5, 6]
    print("Origin List:", list_origin)
    print( "Element 's address:", hex(id(list_origin[0])), hex(id(list_origin[1])), \
            hex(id(list_origin[2])), hex(id(list_origin[3])), \
            hex(id(list_origin[4])), hex(id(list_origin[5])))
    print('Length:', len(list_origin))
    print('Min:', min(list_origin))
    print('Max:', max(list_origin))

    i = 2
    print('Number', i, "appears", list_origin.count(i), "times")

    list_origin.reverse()
    print("After reversing:", list_origin)
    print( "Element 's address:", hex(id(list_origin[0])), hex(id(list_origin[1])), \
            hex(id(list_origin[2])), hex(id(list_origin[3])), \
            hex(id(list_origin[4])), hex(id(list_origin[5])))

    list_origin.sort()
    print("After sorting:", list_origin)
