# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.


import json
json_data = {
    "user":
        [
            {
                "name":"Rajeet",
                "age":22
            },
            {
                "name":"Dell",
                "age":23
            }
        ]
}


print("Serialized")
serialized = json.dumps(json_data, sort_keys= True, indent=4)
print(serialized)

print("Object Created")
object_data = json.loads(serialized)
print(object_data)



