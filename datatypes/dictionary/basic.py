"""
Dictionary
1. Ordered
2. Un indexed(indexed by keys)
3. Mutable


"""
dict1 = {"product": "orange", "product_type": "fruit", "weight": 10, "price": 50}

# clear()
# dict1.clear()
# print(dict1)


# copy()
# x = dict1.copy()
# print(x)


# get()
# y = dict1.get("weight")
# print(y)
# z = dict1["product_type"]
# print(z)


# items()
# print(dict1.items())
# print(type(dict1.items()))


# keys()
# print(dict1.keys())


# pop()
# x = dict1.pop("product_type")  # this returns the value of popped key
# y = dict1.popitem()
# print(y)
# print(x)
# print(dict1)


# popitem() removes last added key value pair
# dict1.popitem()  # use print(dict1.popitem()) to see the removed key value pair
# print(dict1)


# setdefault("keyword", "value")  1.if keyword exist in dictionary this returns the corresponding value of keyword.
# the "value" does not have any affect in this case. 2.If keyword does not exist in dictionary then this
# 'keyword, value' pair will be added to dictionary.3. If 'value' is not given, keyword will be added with 'None' value.
# case1
# x = dict1.setdefault("product", "mango")
# print(x)
# case2
# dict1.setdefault("total_price", 500)
# print(dict1)
# case3
# dict1.setdefault("is_item_there")
# print(dict1)


# update()
# dict1.update({"total_price": 500})
# print(dict1)


# values
# print(dict1.values())
# dict1["weight"] = 100


# fromkeys()
# x = ("key1", "key2", "key3")
# y = 0
# z = (1, 2, 3)
# dict2 = dict.fromkeys(x, y)
# dict5 = dict.fromkeys(x, z)
# print(dict2)
# print(dict5)
#
# a = ("key1", "key2", "key3")
# dict3 = dict.fromkeys(x)
# print(dict3)
#
# b = {"name2": "sourav", "age": 24, "place": "payyanur"}
# dict4 = dict.fromkeys(b, 25)
# print(dict4)

# zip() method to create dictionary from two lists
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
D = dict(zip(l1, l2))
print(D)
