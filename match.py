print("enter 1 for good morning")
print("enter 2 for good afternoon")
print("enter 3 for good ni8")
greet=int(input())

match greet:
    case 1:
        print('Good morning:')
    case 2:
        print("Good afternoon")
    case 3:
        print("Good ni8")
    case _:
        print("invalid input:")