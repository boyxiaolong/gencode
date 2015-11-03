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

des_file.write("package com.example.allen.muhanmaisi_query;\n")
des_file.write("import org.json.JSONObject;\n")
des_file.write("public class " + class_name + " {\n")
beginstr = ''
memstr = ''
funstr = ''
tojson_str = ''
fromjson = ''
memlst = []
while line:
    line.strip('\n')
    if is_substr(line, '{'):
        beginstr = ''
        memstr = ''
        funstr = ''
        memlst = []
        fromjson = ''
        arr = line.split('{',1)
        class_name = arr[0]
        des_file.write("public class " + class_name + " {\n")
        beginstr = 'public ' + class_name + " (){\n"
        tojson_str = "String tojson() {\n";
        fromjson = "void fromjson(JSONObject json) {\ntry {\n";
    elif is_substr(line, '}'):
        print(beginstr, funstr, memstr)
        des_file.write(beginstr+"}\n")
        des_file.write(funstr)
        des_file.write(memstr)
        tojson_str += "String res = \"\";\ntry{\nJSONObject jsonObject = new JSONObject();\n"
        for data in memlst:
            tojson_str += "jsonObject.put(\"" + data + "\"," + data + "_);\n"
        tojson_str +="res = jsonObject.toString();\n}\ncatch (Exception e){\n}\nreturn res;\n}\n"
        fromjson += "}\ncatch(Exception e) {\n}\n}\n"
        des_file.write(tojson_str)
        des_file.write(fromjson)
        des_file.write("}\n")
    elif is_substr(line, ';'):
        arr = line.split(';', 1)
        tmpstr = arr[0]
        tmpstr = tmpstr.lstrip();
        tokenarr = tmpstr.split(' ')
        vari_type = tokenarr[0]
        ori_name = tokenarr[1]
        vari_name = ori_name  + "_"
        memlst.append(ori_name)
        print(vari_name, vari_type)
        if vari_type == "int":
            beginstr += "   " + vari_name + " = 0;\n"
        funstr += vari_type + " get_" + vari_name + "(){\n    return " + vari_name + ";\n}\n"
        funstr += "void set_" + vari_name + "(" + vari_type + " " + ori_name + "){\n" + vari_name + " = " + ori_name + ";\n}\n"
        memstr += vari_type + " " + vari_name + ";\n"
        if "String" == vari_type:
            fromjson += vari_name + "= json.getString(\"" + ori_name + "\");\n"
            aa

    line = msg_file.readline()

des_file.write("}")
msg_file.close()
des_file.close()