numbers=[3,5,6,7,5,9,3]
unique=[]
for item in numbers:
    if item not in unique:
        unique.append(item)
print(unique)        