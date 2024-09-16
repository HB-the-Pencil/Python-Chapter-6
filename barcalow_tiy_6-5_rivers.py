# Make a dictionary of rivers and the countries (or cities) they're in.
rivers = {
    "missouri": "united states",
    "st. joseph": "fort wayne",
    # And now I'm out of rivers that aren't in the US.
    "amazon": "south america",
    "yangtze": "china",
}

# Print a statement of where each river is located. I always forget .items().
for river, location in rivers.items():
    print(f"The {river.title()} river is in {location.title()}.")

# Print a list of the rivers.
print()
print("Rivers included in the dictionary:")
for river in rivers:
    print(river.title())

# Print a list of the locations.
print()
print("Locations mentioned:")
for location in rivers.values():
    print(location.title())