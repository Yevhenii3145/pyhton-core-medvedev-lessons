import json

obj = {"name": "Jack", "age": 21, "brothers": ("Mark", "Mike"), "access": None}
# при сериализации None -> null  () -> []  классы, функции и сеты нельзя сериализовать


serialized = json.dumps(obj)
# {"name": "Jack", "age": 21, "brothers": ["Mark", "Mike"], "access": null}
print(serialized)
print(type(serialized))  # <class 'str'>
deserialized = json.loads(serialized)
# {'name': 'Jack', 'age': 21, 'brothers': ['Mark', 'Mike'], 'access': None}
print(deserialized)

with open("test.json", "w") as file:
    json.dump(obj, file)
