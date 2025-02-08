
print("WITHOUT NESTED LOOP")
number=[1,1,1,1,1,7]
for count in number:
    print('X' * count)
    
    
print("WITH NESTED LOOP") 

for count in number:
    output=''
    for count2 in range(count):
        output+="X"
    print(output)   