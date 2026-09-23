import json

from Dto.User import User

body = """{
    "id": 1,
    "name": "Ayn",
    "email": "ayn@gmail.com"
}"""

# JSON string → Python object
res_obj = json.loads(body)

print("Response:", res_obj)
print("Response Type:", type(res_obj))

# Python object → JSON string
json_string = json.dumps(res_obj)

print("JSON String:", json_string)
print("JSON String Type:", type(json_string))

# create user object
user = User(1,"Ayn","ayn1@gmail.com")

# here you can directly print user, you need to convert in dict and then print
# two ways can convert
# 1- json.dumps(user.__dict__)
# 2- to create a function on model name as to_dict(self): return {"id":self.id ect...}
# python object to json string
user_dict=json.dumps(user.__dict__)
print("User __dict__", user_dict)
user_to_dict = json.dumps(user.to_dict())
print("User : ",user_to_dict)

# test case more than one user
user1 = User(1,"Ayn","ayn1@gmail.com")
user2 = User(2,"Uddin","ayn2@gmail.com")
user3 = User(3, "David", "david@gmail.com")
user_list = [user1,user2,user3]
user_list_dict = [usr.to_dict() for usr in user_list]
print(user_list_dict)

