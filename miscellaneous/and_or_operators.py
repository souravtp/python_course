"""In Python, the and operator returns the first operand if it evaluates to False,
and the second operand otherwise. In this case, since 2 is a non-zero value, it is considered True,
and so the expression evaluates to the second operand 3."""
print(2 and 3)
# print(0 and 3)
# print(False and 3)

"""for bitwise operation it is different"""
print(2 & 3)


"""The output of print(2 or 3) in Python would be 2.

This is because the or operator returns the first truthy value it encounters,
or the last value if none of the values are truthy. In this case, 2 is truthy, so it is returned."""
print(2 or 3)
print(0 or False)
print(False or 0)

"""joining two dictionaries"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}

print(dict3)

from typing import List

# class Solution:
#     def two_sums(self, nums:List[int], target: int) -> List[int]:
#         mapping = []
#         for i in range(len(nums)):
#             x = target - nums[i]
#             if x in map:
#                 return i, mapping.index(x)

# my_list = ['a', 'b', 'c']
# # print(my_list.index('b'))
# x = enumerate(my_list)
# # print(list(x))
# my_dict = {key: value for key, value in x}
# print(my_dict)
