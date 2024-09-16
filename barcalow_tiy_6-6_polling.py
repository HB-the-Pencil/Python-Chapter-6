# Code copied from Favorite Languages practice.
favorite_languages = {
    "ian": "c++",
    "brian": "c#",
    "adam": "basic",
    "charlie": "rust",
}

# Who do we need to take the survey?
people_to_survey = [
    "ian",
    "john",
    "michael",
    "adam",
    "charlie",
    "bill"
]

for name in people_to_survey:
    if name in favorite_languages:
        print(f"Thank you for responding, {name.title()}!")
    else:
        print(f"{name.title()}, you still need to respond to the survey.")