import os
from prettytable import PrettyTable

def display_table():
    base_dir = "car_data"
    all_brands = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    if not all_brands:
        print("No car data available.")
        return

    # Создаем таблицу
    table = PrettyTable()
    table.field_names = ["ID", "Model", "Year", "Color", "Price"]

    for brand in all_brands:
        brand_path = os.path.join(base_dir, brand)
        files = [f for f in os.listdir(brand_path) if f.endswith('.txt')]

        for file in files:
            file_path = os.path.join(brand_path, file)

            with open(file_path, 'r') as f:
                data = f.readlines()

                # Проверяем формат данных и наличие всех строк
                if len(data) >= 5:
                    try:
                        car_id = data[0].split(":")[1].strip() if ":" in data[0] else "Unknown"
                        model = data[1].split(":")[1].strip() if ":" in data[1] else "Unknown"
                        year = data[2].split(":")[1].strip() if ":" in data[2] else "Unknown"
                        color = data[3].split(":")[1].strip() if ":" in data[3] else "Unknown"
                        price = data[4].split(":")[1].strip() if ":" in data[4] else "Unknown"
                    except IndexError:
                        print(f"Error processing file: {file}")
                        continue

                    # Добавляем строку с данными в таблицу
                    table.add_row([car_id, model, year, color, price])
                else:
                    print(f"File {file} is missing data or improperly formatted.")

    # Печатаем таблицу
    print(table)
