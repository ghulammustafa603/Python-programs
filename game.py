secret_no=5
print("*Note you have only 3 attempts!")
i=0
while(i<3):
    takeNo=int(input("Enter guessed number:"))
    if(takeNo==secret_no):
        print(f"wow congrats! guessed number is {takeNo}")
        break
        
    else:
         print(f"ops ! guessed number is not {takeNo}")
         
    i+=1
print("Thanks")        