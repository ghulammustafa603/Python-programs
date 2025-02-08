secret_no=5
print("*Note you have only 3 attempts!")
i=0
while(i<3):
        takeNo=input("Enter  one digit guessed number:")
        if(int(takeNo)==secret_no):
            print("wow congrats! guessed number is ",takeNo)
            break
        else:
            print("ops ! guessed number is not ",takeNo)
        i+=1
print("Thanks")        