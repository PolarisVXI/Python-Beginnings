# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'Caden',
    'last_name' : 'Abbitt',
    'age' : 17
}

# use constructor
person2 = dict(first_name='Mark', last_name='Strong')

# Get value
print(person['age'])
        #OR
print(person.get('last_name'))

# Add key/value
person['phone'] = '512-660-9624'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age' : 30},
    {'name' : 'Kevin', 'age' : 25}
]

print(people[1])




print(type(person), person2)
