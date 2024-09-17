# To make it faster, I'm going to create a list of pet types, pet names, and
# owner names, and then I'm going to loop through them and add them to
# a list of dictionaries.
pet_types = ["dog", "cat", "turtle", "bird", "anaconda"]
pet_names = ["annie", "mercury", "steve", "johnny", "monty"]
owner_names = ["carmen", "andrew", "thomas", "brendon", "matt"]
pets = []

# Loop through the lists and create a list of dictionaries.
for i in range(len(pet_types)):
    pet = {
        "type": pet_types[i],
        "name": pet_names[i],
        "owner": owner_names[i]
    }
    pets.append(pet)

# Loop through the list of pets and print info about each pet.
for pet in pets:
    owner = pet["owner"].title()
    pet_type = pet["type"]
    pet_name = pet["name"].title()
    # Basic grammar checker. If the first letter is a vowel, "an"; else, "a".
    vowels = ["a", "e", "i", "o", "u"]
    article = "an" if pet_type[:1] in vowels else "a"
    print(f"{owner} owns {article} {pet_type} named {pet_name}.")