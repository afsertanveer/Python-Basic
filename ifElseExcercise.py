name = input("Enter your Name: ")
if len(name)<3 :
    print("Too Short Name")
elif len(name)>=50:
    print("Maximum Character 50")
else:
    print("Name Looks Good")