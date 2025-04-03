
d1 = {}
d2 = {}

n1 = int(input("Enter number of elements for first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

n2 = int(input("Enter number of elements for second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

merged_dict = {**d1, **d2}
print("Merged Dictionary:", merged_dict)
