nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""list1 = []
for n in nums:
    for i in "abc":
        list1.append((n, i))
print(list1)"""

# my_list = [(i, n) for i in "abc" for n in nums]
# print(my_list)

# for n in nums:
# if n % 2 == 0:
#   print(n)

# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)
# my_list = map(lambda n: n * n, nums)
# print(list(my_list))
tuple1 = ("zain", "saad", "osama")
tuple2 = ("batsman", "superman", "firehorse")
# zipss = zip(tuple1, tuple2)
# print(tuple(zipss))
my_dict = {}
for tuple1, tuple2 in zip(tuple1, tuple2):
    my_dict[tuple1] = tuple2
print(my_dict)
