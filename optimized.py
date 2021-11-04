def optimized(capacite, action):
    best_action = []

    sorted(action, key=lambda x: x['profit'], reverse=True)

    for x in action:
        if action['price'] <= capacite:
            capacite = capacite - action['price']
            best_action.append(x)
    return best_action
