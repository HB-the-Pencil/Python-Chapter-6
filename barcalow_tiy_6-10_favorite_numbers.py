from math import factorial

# Copied list from TIY 6-2 (Favorite Number).
favorite_nums = {
    "ethan": [7, 2, factorial(8)],
    "day": [17, 11, 35],
    "melody": [2, 13],
    "brodie": [10, 9, 8, 12, 16, 21, 22, 32],
    "audrina": [7, 21],
    "marvellous": [14],
    "okkar": [7],
}

# Loop through the list and print each person's favorite numbers.
for name in favorite_nums:
    # Create a simpler reference to the number list.
    nums = favorite_nums[name]
    # Add some subject-verb agreement.
    is_are = "s are" if len(nums) > 1 else " is"
    print(f"{name.title()}'s favorite number{is_are}", end=" ")

    # See, Mr. McKinstry, this is why I had a library... this function comes
    # up so often. But this did point out potential errors in my function; I
    # modified it to add a str() call to the function.
    for num in nums:
        # If it's before the next-to-last place, add a comma to the end.
        if nums.index(num) < len(nums) - 2:
            print(num, end=", ")
        # If it's the next to last place, add "and".
        elif nums.index(num) < len(nums) - 1:
            # Omit the comma if the list length is two.
            if len(nums) == 2:
                print(num, end=" and ")
            else:
                print(num, end=", and ")
        # If it's the last place, add a period and a newline.
        else:
            print(num, end=".\n")