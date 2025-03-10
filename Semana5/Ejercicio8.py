list_of_keys = ['access_level', 'age']
employee = {'name': 'Josias', 'email': 'josiascr14@.com', 'access_level': 5, 'age': 20}

for keys in list_of_keys:
    if keys in employee:
        del employee[keys]

print(employee)