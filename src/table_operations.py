import os
from prettytable import PrettyTable

def display_table():
    base_dir = "car_data"
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    if not folders:
        print("No car brands available.")
        return
    
    table = PrettyTable()
    table.field_names = ["Brand", "Model", "Year", "Color", "Price"]

    for folder in folders:
        files = [f for f in os.listdir(os.path.join(base_dir, folder)) if f.endswith('.txt')]
        for file in files:
            file_path = os.path.join(base_dir, folder, file)
            with open(file_path, "r") as f:
                data = f.readlines()
                model = data[1].split(":")[1].strip()
                year = data[2].split(":")[1].strip()
                color = data[3].split(":")[1].strip()
                price = data[4].split(":")[1].strip()
                table.add_row([folder, model, year, color, price])

    print(table)
