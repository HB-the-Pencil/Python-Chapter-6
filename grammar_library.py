"""This is a library of functions used to make sentences more grammatical.
"""


# Function to add an article adjective to a word.
def add_article(word):
    # Define a list of vowels.
    vowels = ["a", "e", "i", "o", "u"]

    # Return "an" + the word if it starts with a vowel; else, "a" + the word.
    if word[:1] in vowels:
        return f"an {word}"
    else:
        return f"a {word}"


# Function to punctuate a list of items as a sentence.
def punctuate_list(list_of_items):
    # Convert all items into strings so they can be concatenated.
    items = [str(item) for item in list_of_items]
    message = ""

    # Loop through the list.
    for item in items:
        # If it's before the next-to-last place, add a comma to the end.
        if items.index(item) < len(items) - 2:
            message += f"{item}, "
        # If it's the next to last place, add "and".
        elif items.index(item) < len(items) - 1:
            # Omit the comma if the list length is two.
            if len(items) == 2:
                message += f"{item} and "
            else:
                message += f"{item}, and "
        # If it's the last place, add a period and a newline.
        else:
            message += f"{item}."

    # Return the message.
    return message
