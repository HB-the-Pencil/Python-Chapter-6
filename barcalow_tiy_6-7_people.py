# Take the dictionaries of people and make them into a list!
gerald = {
    "first_name": "Gerald",
    "last_name": "Smith",
    "age": 18,
    "city": "Leo",
    "pronouns": ["he", "him", "his"],
}

melany = {
    "first_name": "Melany",
    "last_name": "France",
    "age": 17,
    "city": "Dallas",
    "pronouns": ["she", "her", "her"]
}

tod = {
    "first_name": "Tod",
    "last_name": "Lander",
    "age": 34,
    "city": "Philadelphia",
    "pronouns": ["he", "him", "his"]
}

# Store the people in a list.
people = [gerald, melany, tod]

# Loop through the list of people to print info about people.
for person in people:
    # Set variables to the person's values or to default values.
    name = f"{person.get("first_name", "@")} {person.get("last_name", "@")}"
    if "@" in name:
        name = "Missing_Full_Name"
    age = person.get("age", "Missing_Age")
    city = person.get("city", "Missing_City")
    pronouns = person.get("pronouns", ["they", "them", "their"])

    # Print info about the person.
    print(f"{name.title()} is {age} years old. {pronouns[0].title()} "
          f"{"live" if pronouns[0] == "they" else "lives"} in {city}.")