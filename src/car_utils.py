import os

# Создание или выбор папки для хранения информации о машинах
def select_or_create_folder():
    base_dir = "car_data"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    while True:
        print("\n--- Select or Create Car Brand Folder ---")
        print("1. Create a new folder and add car")
        print("2. Use an existing folder and add car")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            folder_name = input("Enter a NEW folder name to store car information: ")
            folder_path = os.path.join(base_dir, folder_name)
            if os.path.exists(folder_path):
                print("Folder already exists. Please choose a different name.")
            else:
                os.makedirs(folder_path)
                print(f"Folder '{folder_name}' created.")
                add_car_to_folder(folder_path)  # Добавляем машину после создания новой папки
                return folder_path

        elif choice == '2':
            if folders:
                print("\nAvailable Car Brand Folders:")
                for i, folder in enumerate(folders, start=1):
                    print(f"{i}. {folder}")
                try:
                    folder_choice = int(input("Enter the number of the folder you want to use (or 0 to go back): ")) - 1
                    if folder_choice == -1:
                        continue  # Возвращаемся к выбору меню
                    if 0 <= folder_choice < len(folders):
                        folder_path = os.path.join(base_dir, folders[folder_choice])
                        add_car_to_folder(folder_path)  # Добавляем машину в существующую папку
                        return folder_path
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No existing folders available. Please create a new folder.")

        elif choice == '3':
            print("Returning to the main menu.")
            return '0'  # Возвращаемся в главное меню

        else:
            print("Invalid choice. Please try again.")


def add_car_to_folder(folder_name):
    """Функция для добавления машины и сохранения информации в выбранную папку."""
    
    def validate_input(prompt, validation_func, error_message):
        while True:
            value = input(prompt).strip()
            if validation_func(value):
                return value
            print(error_message)

    # Функции для проверки ввода
    def is_valid_car_id(car_id):
        return bool(car_id.strip())  # Проверка, что строка не пустая

    def is_non_empty_string(input_str):
        return bool(input_str.strip())  # Проверяем, что строка не пустая

    def is_valid_year(year):
        return year.isdigit() and len(year) == 4  # Проверяем, что год состоит из 4 цифр

    def is_valid_color(color):
        return color.isalpha()  # Проверяем, что цвет содержит только буквы

    def is_valid_price(price):
        try:
            return float(price) > 0  # Проверка, что цена - положительное число
        except ValueError:
            return False

    # Добавляем информацию о машине
    car_id = validate_input("Enter the Car ID: ", is_valid_car_id, "Car ID cannot be empty.")
    car_model = validate_input("Enter the Car Model: ", is_non_empty_string, "Car Model must be a valid non-empty string.")
    car_year = validate_input("Enter the Year of Manufacture: ", is_valid_year, "Year must be a valid 4-digit number.")
    car_color = validate_input("Enter the Color of the Car: ", is_valid_color, "Color must be a valid name without numbers or symbols.")
    car_price = validate_input("Enter the Price of the Car: ", is_valid_price, "Price must be a positive number.")

    # Формируем строку с информацией о машине
    car_info = f"Car ID: {car_id}\nCar Model: {car_model}\nYear of Manufacture: {car_year}\nColor: {car_color}\nPrice: {car_price}\n"

    # Сохраняем информацию
    save_car_info(folder_name, car_id, car_info)
    print(f"Car information saved to folder '{folder_name}'.")


# Пример функции сохранения информации о машине
def save_car_info(folder_name, car_id, car_info):
    file_path = os.path.join(folder_name, f"{car_id}.txt")
    with open(file_path, "w") as file:
        file.write(car_info)
    print(f"Car information saved as '{file_path}'.")


if __name__ == "__main__":
    select_or_create_folder()