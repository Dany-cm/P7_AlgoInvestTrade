import csv


class Action:

    def __init__(self, name, price, profit):
        self.name = name
        self.price = float(price)
        self.profit = float(profit)
        self.priceformatrice = int(self.price * 100)
        self.benefice = self.price * self.profit / 100

    def __str__(self):
        return f"{self.name} - {self.price} - {self.profit}% - {self.benefice}"


def get_info_from_file(file):
    with open(file, newline="") as file:
        reader = csv.DictReader(file)
        records = []
        for row in reader:
            if float(row['price']) > 0:
                records.append(Action(row['name'], row['price'], row['profit']))
        return records
