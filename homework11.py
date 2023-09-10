def get_numbers(age):
    if age < 0:
        return "an invalid age value was passed because age cannot be less than 0"
    elif 1 <= age <= 18:
        return "You are baby"
    elif 19 <= age <= 65:
        return "You have to work"
    else:
        return "Happy retirement"
