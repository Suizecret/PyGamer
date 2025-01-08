def check_guess(user_value, random_value, score):
    if user_value != random_value:
        print(user_value)
        print(random_value)
        difference = max(user_value, random_value) - min(user_value, random_value)
        if user_value > random_value:
            hint = "to High"
        else:
            hint = "to Low"
        score -= difference * 2
        return False, score, hint
    else:
        hint = "You got It"
        return True, score, hint
