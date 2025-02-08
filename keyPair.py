phone=input("phone:")
number_Mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for num in phone:
    output+=number_Mapping.get(num,"not present")
    
print(output)