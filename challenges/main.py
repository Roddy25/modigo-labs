def build_profile(name, age, city):
    """
    Takes a name, age, and city, and returns a formatted
    introduction string.
    """
    learner_name = name
    learner_age = age
    learner_city = city

    # TODO: build the introduction string using an f-string
    # Format must be exactly:
    # "Hi, I'm {name}, I'm {age} years old, and I live in {city}."
    intro = f"Hi, I'm {name}, I'm {age} years old, and I live in {city}."  # TODO: replace this with the correct f-string

    return intro
print(build_profile("Ada", 22, "lagos"))