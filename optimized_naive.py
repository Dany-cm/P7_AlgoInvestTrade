def optimized_naive(capacity, actions):
    """ Sort by profit in descending order """

    best_action = []

    sorted(actions, key=lambda x: x.profit, reverse=True)

    for action in actions:
        if action.price <= capacity:
            capacity = capacity - action.price
            best_action.append(action)
    return best_action
