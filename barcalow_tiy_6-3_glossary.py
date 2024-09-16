# We can't call this a dictionary... because it's in a dictionary.
# So instead, let's make a glossary of computer terms.
glossary = {
    "if": "A loop that runs if a condition is true.",
    "elif": "A loop that runs if the previous condition is false and the "
    "current condition is true.",
    "else": "A loop that runs if none of the previous conditions are true.",
    "and": "A logic operator that checks if two conditions are true.",
    "or": "A logic operator that checks if at least one condition is true.",
    "print": "A function that tells Python to print the string or variable "
    "inside the parentheses."
}

# Loop through the glossary. It's much faster than printing them by hand.
for term in glossary:
    # Each definition is on a new line with an indent.
    print(f"{term}:\n\t{glossary[term]}\n")