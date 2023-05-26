import json

"""
json(javascript object notation)
--------------------------------
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
"""
# print(dir(json))

"""convert python to json."""
# x = {"name2": "sourav", "age": 24, "course": "python"}
# print(type(x))
# y = json.dumps(x)  # this converts python to json.
# print(type(y))


"""convert json to python."""
# a = '{"name2": "sourav", "age": 24, "course": "python"}'  # '' around dictionary denotes it is a json data.
# print(type(a))
# b = json.loads(a)
# print(type(b))

"""write a python program to convert python objects to json strings. print all the values"""
# plist = ["apple", "orange", "mango"]
# ptuple = ("suzuki", "toyota", "hyundai")
# pstring = "Hello, world"
# pint = 245
# pfloat = 5.735
# pbool = True
#
# jlist = json.dumps(plist)
# jtuple = json.dumps(ptuple)
# jstring = json.dumps(pstring)
# jint = json.dumps(pint)
# jfloat = json.dumps(pfloat)
# jbool = json.dumps(pbool)
#
# print(type(jlist))
# print(jtuple)

"""pgm to convert python dictionary object(sort by key) to JSON data. print object members with indent level 4."""
# py_dict = {"fruit": "apple", "car": "alto", "age": 30, "key": True}
# j_dict = json.dumps(py_dict, sort_keys=True, indent=4)
# print(j_dict)

"""pgm to convert JSON encoded data into python objects."""
# json_obj1 = '["apple", "orange", "mango"]'
# json_obj2 = '"Hello"'
# json_obj3 = '123'
# json_obj4 = '["car", "auto", "bus", "truck"]'
#
# python_data1 = json.loads(json_obj1)
# print(python_data1)
# python_data2 = json.loads(json_obj2)
# print(python_data2)
# python_data3 = json.loads(json_obj3)
# print(python_data3)
# print(type(python_data3))
# python_data4 = json.loads(json_obj4)
# print(tuple((python_data4)))
