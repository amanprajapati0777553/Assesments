import copy
# SHALLOW COPY
original = [[10,20],[30,40]]
shallow = copy.copy(original)
print("Original :", original)
print("Shallow :", shallow)
print(id(original[0]))
print(id(shallow[0]))
print(original)
print(shallow)
print("After changing in shallow copy")
shallow[0][0] = 100
print("Original :", original)
print("Shallow :", shallow)