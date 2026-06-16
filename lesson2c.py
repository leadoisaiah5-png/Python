# python dictionary
person ={
    "firstname" : "John" ,
    "lastname"  :  "Doe" ,
    "age"  : 22 ,
    "salary"  : 44000 ,
    "favorite colors"  : ["blue", "green"]

}
print(person)

# accessing key value 
print(person["firstname"])
print(person["lastname"])

# update key value parts
person["age"] =34
print(person)

person["firstname"] = "isaiah"
print(person)
person["lastname"] = "leado"
print(person)

# adding a new key value pair
person["passport"] = "BN200KN"
print(person)

# delete the salary 
del person["salary"]
print(person)

del person["firstname"]
print(person)