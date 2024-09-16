# Hehehe... I already used a loop. I'll use a different version this time.
glossary = {
    "if": "A loop that runs if a condition is true.",
    "elif": "A loop that runs if the previous condition is false and the "
        "current condition is true.",
    "else": "A loop that runs if none of the previous conditions are true.",
    "and": "A logic operator that checks if two conditions are true.",
    "or": "A logic operator that checks if at least one condition is true.",
    "print": "A function that tells Python to print the string or variable "
        "inside the parentheses.",
    # New terms below this comment.
    "sorted": "A function that temporarily sorts the items in a list.",
    "set": "A list with no duplicate items, defined using curly braces.",
    "tuple": "An immutable list, defined using parentheses.",
    "dictionary": "A list of values that are assigned to keys.",
    "key": "The string representing the location of a value in a dictionary.",
    "value": "The data stored at the location of a key in a dictionary."
}

# Loop through the glossary using the key-value method.
for term, definition in sorted(glossary.items()):
    print(f"{term}:\n\t{definition}\n")