import os

# Создание или выбор папки для хранения информации о машинах
def select_or_create_folder():
    base_dir = "car_data"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    while True:
        print("\n--- Select or Create Car Brand Folder ---")
        print("1. Create a new folder")
        print("2. Use an existing folder")
        choice = input("Enter your choice: ")

        if choice == '1':
            folder_name = input("Enter a NEW folder name to store car information: ")
            folder_path = os.path.join(base_dir, folder_name)
            if os.path.exists(folder_path):
                print("Folder already exists. Please choose a different name.")
            else:
                os.makedirs(folder_path)
                print(f"Folder '{folder_name}' created.")
                return folder_path

        elif choice == '2':
            if folders:
                print("\nAvailable Car Brand Folders:")
                for i, folder in enumerate(folders, start=1):
                    print(f"{i}. {folder}")
                try:
                    folder_choice = int(input("Enter the number of the folder you want to use: ")) - 1
                    if 0 <= folder_choice < len(folders):
                        return os.path.join(base_dir, folders[folder_choice])
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No existing folders available. Please create a new folder.")

        else:
            print("Invalid choice. Please try again.")

# Проверка уникальности Car ID и его сохранение
def check_and_save_car_id():
    while True:
        print("\n--- Enter Car ID ---")
        car_id = input("Enter the Car ID (unique): ")

        if os.path.exists("CarsID.txt"):
            with open("CarsID.txt", "r") as f:
                existing_ids = f.read().splitlines()
        else:
            existing_ids = []

        if car_id in existing_ids:
            print("Invalid input: This Car ID already exists. Please use a unique ID.")
        else:
            with open("CarsID.txt", "a") as f:
                f.write(car_id + "\n")
            print(f"Car ID '{car_id}' saved successfully.")
            return car_id

# Сохранение информации о машине
def save_car_info(folder_name, car_id, car_info):
    file_path = os.path.join(folder_name, f"{car_id}.txt")
    with open(file_path, "w") as car_file:
        car_file.write(car_info)
    print(f"\nCar information saved in '{file_path}'\n")
