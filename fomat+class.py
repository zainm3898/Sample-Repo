# format
from mimetypes import init


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person("zain", "23")
sentence = " i am {0.name} and my age is {0.age}".format(p1)
print(sentence)
