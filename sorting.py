from __future__ import absolute_import


list1 = [-2, -7, 5, 788, 8]
list1.sort()
print(list1)
dict1 = {"name": "zain", "age": 21, "designation": "software engineer"}
dict_1 = sorted(dict1, reverse=True)
print(dict_1)
list_1 = sorted(list1, key=abs)
print(list_1)
