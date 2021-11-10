def bruteforce(capacity, actions_available, actions_selected=[]):
    """Find all possible possibilities given the capacity"""

    if actions_available:
        benefice_1, actions_for_benefice_1 = bruteforce(capacity, actions_available[1:], actions_selected)
        currentvalue = actions_available[0]

        if currentvalue.price <= capacity:
            benefice_2, actions_for_benefice_2 = bruteforce(capacity - currentvalue.price, actions_available[1:],
                                                            actions_selected + [currentvalue])

            if benefice_1 < benefice_2:
                return benefice_2, actions_for_benefice_2

        return benefice_1, actions_for_benefice_1
    else:
        return round(sum([i.price * i.profit / 100 for i in actions_selected]), 2), actions_selected
