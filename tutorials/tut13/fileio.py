def reading_keyboard_input():
    input_string = input("Enter your input: ")
    print(input_string)

def opening_file():
    file_object = open("resources/fileio.html", 'r+')

    print("Name of the file: ", file_object.name)

    # file_object.close()
    print('Closed or not: ', file_object.closed)

    print('Opening mode: ', file_object.mode)
    print("Softspace flag : ", file_object.softspace)

    file_object.close()

def reading_file():
    fo = open("resources/reading_file.txt", "r+")
    print("Open file ", fo.name)

    print("Read the whole buffer")
    strings = fo.read()
    print(strings)

    position = fo.tell()
    print("Current position: ", position)

    fo.seek(-position, 1)
    position = fo.tell()
    print("After re-position: ", position)

    print("Read 10 characters")
    strings = fo.read(10)
    print(strings)

    position = fo.tell()
    print("Current position: ", position)

    fo.close()

def writing_file():
    fo = open("resources/fileio.html", 'wb')

    fo.write("<!DOCTYPE html>\n")
    fo.write("<html>\n")

    fo.write("\t<head>\n")

    fo.write("\t\t<style>\n")    
    lines = ["\t\t\tbody {background-color: powderblue}\n",
            "\t\t\th1 {color: blue; border: 2px solid purple}\n",
            "\t\t\tp {color: red}\n"]    
    fo.writelines(lines)
    fo.write("\t\t</style>\n")

    fo.write("\t</head>\n")

    fo.write("</html>\n")

    fo.close()

def os_module():
    import os

    txt_dir = "resources/txt"
    html_dir = "resources/html"
    print("Making 2 new directories: ", txt_dir, " and ", html_dir)
    os.mkdir(txt_dir)
    os.mkdir(html_dir)    

    txt_file_name = "resources/writing_file.txt"
    print("Original file name:", txt_file_name)

    new_file_name = txt_dir + "/writing_file.txt"
    os.renames(txt_file_name, new_file_name)
    print("Rename: ", new_file_name)
