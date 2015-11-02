__author__ = 'allen'

import sys
import os

def is_substr(ori_str, sub_str):
    return ori_str.find(sub_str) > -1
msgfile_name = "msg.txt"
msg_file = ""
try:
    msg_file = open(msgfile_name)
except Exception,e:
    print("read file error")

line = msg_file.readline()

index = msgfile_name.find(".txt")
print(index)
class_name = msgfile_name[0:index]
des_file_name = class_name + '.python'
des_file = open(des_file_name, "wb+")

des_file.write("public final class " + class_name + " {\n")
beginstr = ''
memstr = ''
funstr = ''
while line:
    line.strip('\n')
    if is_substr(line, '{'):
        beginstr = ''
        memstr = ''
        funstr = ''
        arr = line.split('{',1)
        class_name = arr[0]
        des_file.write("public final class " + class_name + " {\n")
        beginstr = 'public ' + class_name + " {\n"
    elif is_substr(line, '}'):
        print(beginstr, funstr, memstr)
        des_file.write(beginstr+"}\n")
        des_file.write(funstr)
        des_file.write(memstr)
        des_file.write("}\n")
    elif is_substr(line, ';'):
        arr = line.split(';', 1)
        tmpstr = arr[0]
        tmpstr = tmpstr.lstrip();
        tokenarr = tmpstr.split(' ')
        vari_type = tokenarr[0]
        vari_name = tokenarr[1] + "_"
        print(vari_name, vari_type)
        if vari_type == "int":
            beginstr += "   " + vari_name + " = 0;\n"
        funstr += vari_type + " get_" + vari_name + "(){\n    rerurn " + vari_name + ";\n}\n"
        memstr += vari_type + " " + vari_name + ";\n"
        print(beginstr, funstr, memstr)

    line = msg_file.readline()

des_file.write("}")
msg_file.close()
des_file.close()