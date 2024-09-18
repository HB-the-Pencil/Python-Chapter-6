"""TODO
[X] Create a Dictionary from the two lists where candy_type is the key and
    candy_price is the value.

[X] Check for Duplicate candy types

[X] Remove any candy that costs more than $3.00

[X] Add a new value to the dictionary and that tells me if the candy is
    chocolate or some other type of candy. (You might have to research this
    and manually enter this.)

[X] Print out all candy that is chocolate and remind me to make sure to keep
    refrigerated.

[X] In a docstring explain why it is easier to use the candy data in a
    dictionary than it was in a list. Also, explain when and why we use lists
    and dictionaries.
"""

import csv
from difflib import SequenceMatcher  # This is used for string matching later.

# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)
    print(candy_type)
    print(candy_price)


# Function used to compare two strings.
def compare_strings(str1, str2, precision=0.75):
    # Convert strings 1 and 2 to an alphabetically sorted version of itself.
    # The strings need to be sorted because otherwise the SequenceMatcher
    # function only compares the sequences of characters (thus, if they were
    # scrambled, there would be less of a match).
    str1 = sorted(list(str1))
    str1_concat = ""
    for char in str1:
        str1_concat += char
    str1 = str1_concat

    str2 = sorted(list(str2))
    str2_concat = ""
    for char in str2:
        str2_concat += char
    str2 = str2_concat

    # Now compare them with SequenceMatcher. Is it more than an 80% match?
    return SequenceMatcher(None, str1, str2).ratio() >= precision

# Clean the data. This will remove duplicates when put into the dictionary
# (since there's only one value per key).
candy_type = [candy.strip().lower() for candy in candy_type]

# Define an empty dictionary for the candy.
candy_dict = {}

for i in range(len(candy_type)):
    # Create a new key for each candy name with the value as the candy price.
    candy_dict[candy_type[i]] = candy_price[i]

print(candy_dict)

# I had to check StackOverflow for like 15 minutes to find a way to compare
# the ratio of similarity between two strings.
for candy in candy_type:  # The dictionary gets modified, so we can't use it.
    for candy_check in candy_type:
        # If the candy we're checking is the candy we're checking against,
        # or the candy we're checking has already been removed, continue.
        if candy == candy_check or candy_check not in candy_dict:
            continue
        if compare_strings(candy, candy_check):
            print(f"{candy} is at least a 75% match to {candy_check}")
            if candy in candy_dict:
                del candy_dict[candy]

# AT LAST! That took far too long.
print(candy_dict)

# Delete any items costing more than three dollars.
candies_over_three = []
for index, cost in candy_dict.items():
    if cost > 3.0:
        candies_over_three.append(index)
for index in candies_over_three:
    del candy_dict[index]

print(candy_dict)

# Create a new key for each item saying whether it is chocolate.
for candy, data in candy_dict.items():
    new_data = {"price": data, "is_chocolate": False}
    candy_dict[candy] = new_data

# Loop through the list. If the item matches the list of chocolate candies,
# set "is_chocolate" to true.

chocolate_candies = [
    "almond joy",
    "hershey's special dark zero sugar chocolate bar",
    "reeces",
    "3 musketeers",
    "milky way",
    "twix",
    "snicker",
    "heath bar",
    "reese's chocolate",
    "hersheys candy bar",
    "cookie n cream hershey king size bar"
]

for candy, values in candy_dict.items():
    if candy in chocolate_candies:
        values["is_chocolate"] = True

print(candy_dict)

# Print out a reminder to put the chocolate candies in the fridge. (This was
print("Remember to refrigerate ", end="")
for candy, values in candy_dict.items():
    if values["is_chocolate"]:
        print(f"{candy.title()},", end=" ")

# This is a cheater way to hide the fact that I didn't punctuate this list
# properly. There's no index in dictionaries.
print("and any other chocolate candies you might have.")

""" Using Dictionaries vs Using Lists

Dictionaries are far more useful than lists for storing data. Dictionaries
take a key, not just an index, making it easy to remember where data is stored
(you don't just have to use a random index). Both dictionaries and lists are
iterable, meaning they can be looped through. This makes it easy to quickly
test all values in a list (or dictionary).

Lists and dictionaries are useful for storing large amounts of data in a
format that allows for easy modification.

"""
