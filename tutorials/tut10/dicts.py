def dictionary_define_and_access():
    dict = {'Name':'Akagi', 'Age': 33, 'Hometown': 'Quy Nhon city'}
    print(dict)
    print('Name:', dict['Name'])
    print('Age:', dict['Age'])
    print('Hometown:', dict['Hometown'])

    print('----------------------------')
    dict = {1: 'Akagi', 2: 'Yushin', 3: 'Mogami'}
    print(dict)
    print('Number 1:', dict[1])
    print('Number 2:', dict[2])
    print('Number 3:', dict[3])  
    try:
        print('Number 4:', dict[4])
    except Exception as e:
        print('Error:', e)

def dictionary_update():
    dict = {'Name':'Akagi', 'Age': 33, 'Hometown': 'Quy Nhon city'}
    print('Original dictionary:', dict)

    dict['Major'] = 'Mechatronics'
    dict['Languages'] = ['Vietnamese', 'English', 'Japanese']
    print('Updated dictionary:', dict)

    dict['Name'] = 'Yushin'
    print('Updated dictionary:', dict)

def dictionary_delete():
    dict = {'Name':'Akagi', 'Age': 33, 'Hometown': 'Quy Nhon city'}
    print('Original dictionary:', dict)

    del dict['Name']
    print('After removing Name:', dict)

    dict.clear()
    print('After dict.clear():', dict)

    del dict
    try:
        print('After del dict:', dict)
    except Exception as e:
        print('Catched error:', e)

def dictionary_built_in_funcs():
    dict = {'Name':'Akagi', 'Age': 33, 'Hometown': 'Quy Nhon city'}
    print('Original dictionary:', dict)
    print('Length of dictionary:', len(dict))

    copied_dict = dict.copy()
    print('Copied dictionary:', copied_dict)
