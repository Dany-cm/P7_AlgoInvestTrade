import csv


def get_info_from_file(file):
    """Get information from a selected file"""
    with open(file, newline="") as file:
        reader = csv.DictReader(file)
        action_list = []
        for row in reader:
            if float(row["price"]) > 0:
                action_list.append([row["name"], 
                float(row["price"]), (float(row["price"]) * float(row["profit"]) / 100)])
        return action_list
