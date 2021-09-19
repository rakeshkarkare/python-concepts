import json

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["john@email.com", "smith@email.com"],
      "has_licence": false
    },
    {
      "name": "John Doe",
      "phone": "515-555-7164",
      "emails": null,
      "has_licence": true
    }
  ]
}
'''

data = json.loads(people_string)
print(type(data))
print(type(data['people']))

for person in data['people']:
    del person['phone']


new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
