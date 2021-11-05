def optimized(capacite, action):
    """ Sort by profit in descending order """

    best_action = []

    sorted(action, key=lambda x: x[2], reverse=True)

    for x in action:
        if x[1] <= capacite:
            capacite = capacite - x[1]
            best_action.append(x)
    return best_action
