from collections import OrderedDict
foo =input()
r= "".join(OrderedDict.fromkeys(foo))
print(r)
