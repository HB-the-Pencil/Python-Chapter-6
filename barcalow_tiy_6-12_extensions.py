# Haha! I can use my library as a way to improve output formatting!
from grammar_library import punctuate_list

# Make a dictionary of favorite places.
favorite_places = {
    "ethan": ["his upstairs bathroom", "escape rooms", "mountains",
              "Jamaica"],
    "brodie": ["his bedroom", "his dad's house"],
    "melody": ["the McDonald's play-place", "SkyZone"],
    "mr. mckinstry": ["Wrigley field", "Fernandina Beach",
                      "FWCS Career Academy"],
    "henry": ["FWCS Career Academy", "South Side", "home", "in a tree"],
    "sam": ["the Shire"]
}

# Create a set for all the places we mention (so there are no repeats).
places_mentioned = set()

# Loop through the dictionary and print everyone's favorite places.
for person in favorite_places:
    # Assign places list to a variable to make it easier to reference.
    places = favorite_places[person]

    # Make sure there's subject-verb agreement.
    is_are = "s are" if len(places) > 1 else " is"
    print(f"{person.title()}'s favorite place{is_are}", end=" ")

    # Print the list of people's favorite places (using good punctuation).
    print(punctuate_list(places))

    # Add the places in the list to the list of every place mentioned.
    for place in places:
        # A couple of the items included "his" as a specifier, so we need to
        # make it clear whose bedroom or bathroom or whatever it is.
        if "his" in place or "her" in place or "their" in place:
            place = f"{person.title()}'s {place[4:]}"

        # Add the place to the set of places mentioned. Thanks, StackOverflow!
        places_mentioned.add(place)

# Print out a last of every place mentioned.
is_are = "s are" if len(places_mentioned) > 1 else " is"
print(f"Our class's favorite place{is_are}", end=" ")
print(punctuate_list(places_mentioned))  # See, I can use it more than once!