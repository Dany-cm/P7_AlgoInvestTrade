import csv
import time


class Action:

    def __init__(self, name, price, profit):
        self.name = name;
        self.price = int(price);
        self.profit = int(profit);

    def __str__(self) -> str:
        return f"{self.name} - {self.price} - {self.profit}"

    action_list = [];
    possibilities = [];
    
    def get_info_from_file(file):
        with open(file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                Action.action_list.append(Action(row['Actions #'], row['price'], row['profit']))

    def calculate_maximum_profit_via_bruteforce(capacite):
        Action.possibilities = [];
        Action.calculate_with_next_action([], Action.action_list.copy(), capacite)
        Action.possibilities.sort(key=lambda x: sum(y.profit for y in x), reverse=True)
        return Action.possibilities[0]

    def calculate_with_next_action(actions_selected, actions_available, capacite):
        if Action.calculate_total_price(actions_selected) <= capacite:
            Action.possibilities.append(actions_selected)
        else:
            return

        for x in actions_available:
            if Action.check_action_buyable(actions_selected, x, capacite):
                new_actions_selected = actions_selected.copy()
                new_actions_selected.append(x)
                new_actions_available = actions_available.copy()
                new_actions_available.remove(x)
                Action.calculate_with_next_action(new_actions_selected, new_actions_available, capacite)

    def check_action_buyable(actions_selected, action_to_buy, capacite):
        return Action.calculate_total_price(actions_selected) + action_to_buy.price <= capacite

    def calculate_total_price(actions):
        return sum(x.price for x in actions)

Action.get_info_from_file('dataset_1.csv')
start = time.time()
print("".join("\n" + str(x) for x in Action.calculate_maximum_profit_via_bruteforce(500)))
end = time.time()
print(end - start)