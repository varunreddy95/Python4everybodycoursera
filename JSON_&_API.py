import json

#JSON represents data as nested list and dictionaries
data = '''{
        "name" : "Varun",
        "phone" : {
                "type" : "intl",
                "number" : "+1 234 56788"
                },
        "email" : {
            "hide" : "yes"}
        }'''

info = json.loads(data)
print("Name: ", info['name'])
print("Hide: ", info["email"]["hide"])

