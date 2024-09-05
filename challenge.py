phone = input("Phone: ")
digits_mapping ={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}
output = ""
for digit in phone :
    output+=digits_mapping.get(digit,"!") +" "

print(output)