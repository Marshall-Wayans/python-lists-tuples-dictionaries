#Create a dictionary list
dictionary = {
    "name": "Marshal",
    "age" : 22,
    "school" : "Moringa School"
}

print(dictionary)

#Add a ney key-value pair
dictionary.update({"country" : "Kenya"})
print(dictionary)

dictionary["email"] = "marshalwayans@gmail.com"
print(dictionary)

dictionary.update({"country" : "Kenya", "phone" : +254712345678} )
print(dictionary)
S
#update the existing value
dictionary["email"] = "wayansmarshal@gmail.com"
print(dictionary)

#Retrieve and Print a value using a key
print(dictionary["name"])

dictionary.clear()
print(dictionary)