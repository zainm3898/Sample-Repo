from queue import Empty


list1 = [0, 1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]
"""for i in list1:
    for check in list2:
        print(i, check)
for j in range(100):
    if j == 5:
        break
    if j == 4:
        continue
    print(j)
"""
i = 0
while list1 != -1:
    if list1[i] % 2 == 0:
        print("these are even numbers", list1[i])
    else:
        print("these are the odd number", list1[i])
