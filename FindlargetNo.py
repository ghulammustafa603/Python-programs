number=[3,5,6,6,8,3,9,1]
length=len(number)
large=number[0]
for i in number: 
    if(large<i):
        large=i
print(large)