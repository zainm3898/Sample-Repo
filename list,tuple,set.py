list_1 = ["monday", "tuesday", "wednesday"]
# print(list_1)
# print(list_1[0])
# print(list_1[:5])
# print(list_1[7:])
list_1.append("friday")

list_1.insert(0, "sunday")
# print(list_1)
list_2 = ["thursday"]
# list_1.insert(0, list_2)
# print(list_1)
list_1.extend(list_2)
# print(list_1)
list_1.remove("monday")
# print(list_1)print(list_1)
list_1.pop()
# print(list_1)
list_1.sort(reverse=True)
#
# print(list_1)
# print("monday" in list_1)
list_3 = [1, 2, 3, 4, 5, 6]
# for item in list_1:
# print(item)
# for index, item in enumerate(list_1, start=2):
# print(index, item)
list_1 = "-".join(list_1)
# print(list_1)
# print(list_1.split("-"))
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (6, 7, 8, 9, 10)
tuple_1 = tuple_2
print(tuple_1, tuple_2)
list_1 = list_2
print(list_1, list_2)
list_2.append("friday")
print(list_1, list_2)
# tuple_2.insert(10)
print(tuple_1, tuple_2)
set_1 = {1, 2, 5, 4}
set_2 = {5, 6, 7, 8}
print(set_1.intersection(set_2))
