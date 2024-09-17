# Make a dictionary of information about cities.
cities = {
    "fort wayne": {
        "country": "United States",
        "population": 267927,
        "fact": "Fort Wayne is the 83rd largest city in the United States."
    },
    "stockholm": {
        "country": "Sweden",
        "population": 987661,
        "fact": "Stockholm contains over 50 bridges."
    },
    "chicago": {
        "country": "United States",
        "population": int(2.665e6),
        "fact": "Chicago is the 3rd largest city in the United States."
    }
}

# Loop through the dictionaries.
for city in cities:
    # Create an easier reference to the city dictionary.
    city_info = cities[city]
    print(f"Information about {city.title()}:")
    # Print each bit of information about a city.
    for data, value in city_info.items():
        print(f"\t{data.title()}: {value}")
    print()