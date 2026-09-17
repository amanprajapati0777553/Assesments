import copy
# DEEP COPY
original = [[10,20],[30,40]]
deep = copy.deepcopy(original)
print(original is deep)
print(id(original))
print(id(deep))
print(original)
print(deep)
deep[0][0] = 100
print(original)
print(deep)