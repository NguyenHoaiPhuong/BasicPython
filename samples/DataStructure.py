# -*- coding: utf-8 -*-

def ListDefine():
    List = ["Akagi", 1986, "Yushin", 1991]
    print(List)
    print("First Element:", List[0])
    print("Last Element:", List[-1])
    print("Length of the list:", len(List))
    
def ListUpdate():
    List = ["Akagi", 1985, "Yushin", 1991]
    print("Original list:", List)
    print("Original list address:", hex(id(List)))
    print("Original list elements' addresses:", hex(id(List[0])), hex(id(List[1])), hex(id(List[2])), hex(id(List[3])))   
    
    List[1] = 1986
    print("New list:", List)
    print("New list address:", hex(id(List)))
    print("New list elements' addresses:", hex(id(List[0])), hex(id(List[1])), hex(id(List[2])), hex(id(List[3])))    

def ListDelete():
    List = ["Akagi", 1985, "Yushin", 1991]
    print("Original:", List)
    print("Original list address:", hex(id(List)))
    delIdx = 2
    del(List[delIdx])
    print("After deleting element", delIdx, ":", List)
    print("New list address:", hex(id(List)))
    
def ListConcatenate():
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
    print( "list3 elements' addresses:", hex(id(list3[0])), hex(id(list3[1])), hex(id(list3[2])), hex(id(list3[3])), hex(id(list3[4])) )
    
def ListRepeat():
    List = ["Hi"]
    print("Original list:", List)
    
    List *= 4
    print("New list = List * 4:", List)
    
def ListMembership():
    List = [1, 2, 3]
    print("Original list:", List)
    
    isMember = 3 in List
    print("3 is in List ?", isMember)
    
    isMember = 4 in List
    print("4 is in List ?", isMember)
    
def ListIterate():
    List = [1, 2, 3]
    print("Original list:", List)
    
    for i in List:
        print(i)
        
def ListSlicing():
    List = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", List)
    
    newList = List[:2]
    print("new list List[:2]:", newList)
    
    newList = List[2:5]
    print("new list ist[2:5]:", newList)
    
def ListMaxMin():
    List = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", List)
    
    print("Max:", max(List))
    print("Min:", min(List))
    
def ListMethods():
    List = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", List)
    
    List.append(8)
    print("After appending element 8:", List)
    
    List.reverse()
    print("After reversing:", List)
    
    List.sort()
    print("After sorting:", List)