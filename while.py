# questions
# # q1
# i=1
# while(i<=100):
#     print(i)
#     i+=1
# #q2
# i=100
# while(i>=1):
#     print(i)
#     i-=1 

# q3

# num=input("write number whose table you want to print:")

# i=1
# while(i<=10):
#     print(i*int(num))
#     i+=1

# # q4
# numbers=[3,5,2,5,6,3]
# len=len(numbers)
# i=0
# while(i<len):
#     print(numbers[i])
#     i+=1

# q5

nums=[4,6,8,4,7,3,0]
n=input("Enter the number which you want to find:")

i=0
found=False
length=len(nums)
while(i<length):
    if(nums[i]==int(n)):
        print("it is print at index:", i)
    
        found=True   
    else:
        print("findings...")
    i+=1

if(found==False):
    print("Sorry! given number is not present in the list.")

#  q6
sum=0
n=input("Enter the till which you want to print:")
i=1
while(i<=int(n)):
    sum+=i
    i+=1
print("sum=",sum)    
   