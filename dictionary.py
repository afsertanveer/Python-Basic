customer ={
    "name" : "Afser",
    "age" : 30 ,
    "is_verified" : True
} #each key has to be unique and the value can be anything
customer["name"] = "Afser Tanveer"
customer["birthdate"] = "January 2 , 19992"
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate",'January 1, 1999')) #if birthdate value is not defined then it will fill with default value written right after that
