def unify(x, y, substitution={}):

    if substitution is None:
        return None

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        substitution[x] = y
        return substitution

    if isinstance(y, str) and y.islower():
        substitution[y] = x
        return substitution

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


# Main program
expr1 = ("Eats", "x", "Apple")
expr2 = ("Eats", "Riya", "y")

result = unify(expr1, expr2, {})

if result:
    print("Unification Successful")
    print("Substitution:", result)
else:
    print("Unification Failed")