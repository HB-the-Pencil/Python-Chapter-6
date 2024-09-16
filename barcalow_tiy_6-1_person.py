# Make a dictionary of information about Gerald Smith.
person = {
    "first_name": "Gerald",
    "last_name": "Smith",
    "age": 18,
    "city": "Leo",
    "pronouns": ["he", "him", "his"],
}

print(f"My friend's name is "
      f"{person["first_name"].title()} {person["last_name"].title()}. "
      f"{person["pronouns"][0].title()} is {person["age"]} years old "
      f"and lives in {person["city"]}.")
