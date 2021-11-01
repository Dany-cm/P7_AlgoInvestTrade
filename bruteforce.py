import csv

def get_info_from_file(file):

    action_list = []

    with open(file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            action_list.append((row['Actions'], float(row['price']), float(row['profit'])))
            
        return action_list

def bruteforce(capacite, actions_available, actions_selected = []):

    if actions_available:
        profit_1, action_profit_1 = bruteforce(capacite, actions_available[1:], actions_selected)
        currentvalue = actions_available[0]

        if currentvalue[1] <= capacite:
            profit_2, action_profit_2 = bruteforce(capacite - currentvalue[1], actions_available[1:], actions_selected + [currentvalue])

            if profit_1 < profit_2:
                return profit_2, action_profit_2

        return profit_1, action_profit_1
    else:
        return sum([i[2] for i in actions_selected]), actions_selected
