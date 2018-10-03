pet={'name':'Nousis','species':'duck'}
print(pet['name'] + " is a " + pet['species'])
#Insert
pet['age'] = 2
pet['gender'] = 'male'
del pet['gender']
print(pet.items()) #Gives a list of tuples containing (key, value)
print(pet.keys())
print(pet.values())
