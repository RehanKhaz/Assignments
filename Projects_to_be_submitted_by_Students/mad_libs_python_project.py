def madlib():
    # Taking user inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food item: ")
    
    # Madlib Story
    story = f"""
    One day, {name} went to {place}. It was a very {adjective} day.
    Suddenly, a {animal} appeared and started to {verb}.
    Shocked, {name} threw a {food} at it, and the {animal} ran away!
    What a crazy adventure!
    """
    
    # Printing the final story
    print("\nHere is your Mad Lib story:\n")
    print(story)

# Running the function
if __name__ == "__main__":
    madlib()
