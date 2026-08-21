import json

input = '''{
    "name" : "Mukul",
    "phone" : {
    "type" : "intl",
    "number" : "+91 8651088574" 
    },
    "email" : {
    "hide" : "yes"
    }
}'''

info = json.loads(input)
print("Name :",info["name"])
print("Phone :",info["phone"]["number"])
print("Hide :",info["email"]["hide"])