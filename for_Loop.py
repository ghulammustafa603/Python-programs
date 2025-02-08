# str="GHULAM MUSTAFA"
# for i in str:
#     print(i)
# # q1
list=[3,5,2,5,6,7]

# for i in list:
#     print(list[i])

# q2
# n=3
# for i in list:
#     if(i==n):
#         print("Number found at index:",i)
#     else:
#         print("finding....")    

# q3
n=input("Enter the number whose factorial you want to find:")
fact=1
for i in range(int(n),0,-1):
    fact*=int(i)

print(fact)