# from first_library import punctuate_list

# Make a dictionary of favorite places.
favorite_places = {
    "ethan": ["his upstairs bathroom", "escape rooms", "mountains", "Jamaica"],
    "brodie": ["his bedroom", "his dad's house"],
    "melody": ["the McDonald's play-place", "SkyZone"],
    "mr. mckinstry": ["Wrigley field", "Fernandina Beach",
                      "FWCS Career Academy"],
    "henry": ["FWCS Career Academy", "South Side", "home", "in a tree"],
    "sam": ["the Shire"]
}

# Loop through the dictionary and print everyone's favorite places.
for person in favorite_places:
    # Assign places list to a variable to make it easier to reference.
    places = favorite_places[person]

    # Make sure there's subject-verb agreement.
    is_are = "s are" if len(places) > 1 else " is"
    print(f"{person.title()}'s favorite place{is_are}", end=" ")

    # I wrote my own library for this one! Now I have a list punctuation
    # function and an article function. It's only called once here, so I just
    # copied the function code with importing the function.
    for place in places:
        # If it's before the next-to-last place, add a comma to the end.
        if places.index(place) < len(places) - 2:
            print(place, end=", ")
        # If it's the next to last place, add "and".
        elif places.index(place) < len(places) - 1:
            # Omit the comma if the list length is two.
            if len(places) == 2:
                print(place, end=" and ")
            else:
                print(place, end=", and ")
        # If it's the last place, add a period and a newline.
        else:
            print(place, end=".\n")