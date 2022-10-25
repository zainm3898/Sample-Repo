dict_1 = {"name": "zain", "contact": "0239830", "id": 7011}
print(dict_1)
print(dict_1["name"])
del dict_1["name"]
print(dict_1)
dict_1["name"] = "zain"
dict_1["id"] = 7010
print(dict_1)
print(len(dict_1))
print(dict_1.values())
for key, values in dict_1.items():
    print(key, values)
