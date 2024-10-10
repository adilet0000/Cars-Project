##################################
# Author: Melsov Adilet & Adilet #
##################################

import os
import shutil
import glob


# 1. Edit function: Edit file name or its contents
def edit_file():
    view_cars()
    try:
        folder_choice = int(input("\nEnter the number of the folder you want to edit a file in: ")) - 1
        folders = [f for f in os.listdir() if os.path.isdir(f)]
        if 0 <= folder_choice < len(folders):
            selected_folder = folders[folder_choice]
            files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
            if not files:
                print(f"No files in '{selected_folder}'")
                return

            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            file_choice = int(input("\nEnter the number of the file you want to edit: ")) - 1

            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]
                print("1. Rename file")
                print("2. Edit file contents")
                edit_choice = input("Enter your choice: ")

                if edit_choice == '1':
                    new_name = input("Enter the new file name (without extension): ") + '.txt'
                    os.rename(os.path.join(selected_folder, selected_file), os.path.join(selected_folder, new_name))
                    print(f"File renamed to {new_name}")
                elif edit_choice == '2':
                    with open(os.path.join(selected_folder, selected_file), "r+") as f:
                        print("\nCurrent file contents:")
                        print(f.read())
                        f.seek(0)
                        new_content = input("\nEnter the new content: ")
                        f.write(new_content)
                        f.truncate()
                    print(f"File contents updated.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid file choice.")
        else:
            print("Invalid folder choice.")
    except ValueError:
        print("Invalid input.")


# 2. Delete function: Move files to bucket and allow restoration or permanent deletion
BUCKET_FOLDER = "bucket"

def ensure_bucket_exists():
    if not os.path.exists(BUCKET_FOLDER):
        os.makedirs(BUCKET_FOLDER)

def delete_file():
    ensure_bucket_exists()
    view_cars()
    folder_choice = int(input("\nEnter the number of the folder you want to delete a file from: ")) - 1
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    
    if 0 <= folder_choice < len(folders):
        selected_folder = folders[folder_choice]
        files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
        if not files:
            print(f"No files in '{selected_folder}'")
            return

        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        file_choice = int(input("\nEnter the number of the file you want to delete: ")) - 1

        if 0 <= file_choice < len(files):
            selected_file = files[file_choice]
            shutil.move(os.path.join(selected_folder, selected_file), os.path.join(BUCKET_FOLDER, selected_file))
            with open(os.path.join(BUCKET_FOLDER, 'deleted_files_paths.txt'), 'a') as f:
                f.write(f"{selected_file}:{selected_folder}\n")
            print(f"File '{selected_file}' moved to bucket.")
        else:
            print("Invalid file choice.")
    else:
        print("Invalid folder choice.")

def restore_file():
    ensure_bucket_exists()
    bucket_files = [f for f in os.listdir(BUCKET_FOLDER) if f.endswith('.txt') and f != 'deleted_files_paths.txt']
    if not bucket_files:
        print("No files in the bucket.")
        return

    print("\nFiles in the bucket:")
    for i, file in enumerate(bucket_files, start=1):
        print(f"{i}. {file}")

    file_choice = int(input("\nEnter the number of the file to restore: ")) - 1
    if 0 <= file_choice < len(bucket_files):
        selected_file = bucket_files[file_choice]
        with open(os.path.join(BUCKET_FOLDER, 'deleted_files_paths.txt'), 'r') as f:
            paths = f.read().splitlines()

        for path in paths:
            if selected_file in path:
                folder_name = path.split(":")[1]
                shutil.move(os.path.join(BUCKET_FOLDER, selected_file), os.path.join(folder_name, selected_file))
                print(f"File '{selected_file}' restored to '{folder_name}'")
                break
    else:
        print("Invalid file choice.")

def empty_bucket():
    ensure_bucket_exists()
    shutil.rmtree(BUCKET_FOLDER)
    os.makedirs(BUCKET_FOLDER)
    print("Bucket emptied.")


# 3. Backtrack function: Navigate back to previous steps
def backtrack():
    print("Returning to the previous menu...")


# 4. Move files function: Move files between folders
def move_file():
    view_folders()
    folder_choice_src = int(input("Enter the number of the folder to move from: ")) - 1
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    
    if 0 <= folder_choice_src < len(folders):
        src_folder = folders[folder_choice_src]
        files = [f for f in os.listdir(src_folder) if f.endswith('.txt')]
        if not files:
            print(f"No files in '{src_folder}'")
            return
        
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        file_choice = int(input("Enter the number of the file to move: ")) - 1
        
        if 0 <= file_choice < len(files):
            file_to_move = files[file_choice]
            folder_choice_dest = int(input("Enter the number of the folder to move to: ")) - 1
            if 0 <= folder_choice_dest < len(folders):
                dest_folder = folders[folder_choice_dest]
                shutil.move(os.path.join(src_folder, file_to_move), os.path.join(dest_folder, file_to_move))
                print(f"File '{file_to_move}' moved to '{dest_folder}'.")
            else:
                print("Invalid destination folder choice.")
        else:
            print("Invalid file choice.")
    else:
        print("Invalid source folder choice.")


# 5. Search function: Search for files by name
def search_files():
    search_term = input("Enter search term: ")
    results = []
    for root, _, files in os.walk('.'):
        for file in files:
            if search_term.lower() in file.lower():
                results.append(os.path.join(root, file))
    
    if results:
        print("\nSearch results:")
        for result in results:
            print(result)
        file_to_view = input("Enter the path of the file you want to view: ")
        if os.path.exists(file_to_view):
            with open(file_to_view, "r") as f:
                print(f"\n--- File Contents ---")
                print(f.read())
        else:
            print("Invalid file path.")
    else:
        print("No results found.")


# 6. Display car info in table format
def display_table():
    import pandas as pd
    car_data = []
    
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    for folder in folders:
        files = [f for f in os.listdir(folder) if f.endswith('.txt')]
        for file in files:
            with open(os.path.join(folder, file), 'r') as f:
                data = f.read().splitlines()
                car_info = {}
                for line in data:
                    key, value = line.split(': ', 1)
                    car_info[key] = value
                car_info['Brand'] = folder
                car_data.append(car_info)
    
    df = pd.DataFrame(car_data)
    print(df)
    
# Функция для создания новой папки или выбора существующей
def select_or_create_folder():
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    
    while True:
        print("\n--- Select or Create Car Brand Folder ---")
        print("1. Create a new folder")
        print("2. Use an existing folder")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Создать новую папку
            while True:
                folder_name = input("Enter a NEW folder name to store car information: ")
                if os.path.exists(folder_name):
                    print("Folder already exists. Please choose a different name.")
                else:
                    os.makedirs(folder_name)
                    print(f"Folder '{folder_name}' created.")
                    return folder_name
        
        elif choice == '2':
            if folders:
                print("\nAvailable Car Brand Folders:")
                for i, folder in enumerate(folders, start=1):
                    print(f"{i}. {folder}")
                try:
                    folder_choice = int(input("Enter the number of the folder you want to use: ")) - 1
                    if 0 <= folder_choice < len(folders):
                        return folders[folder_choice]
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No existing folders available. Please create a new folder.")
        
        else:
            print("Invalid choice. Please try again.")

# Функция для проверки уникальности Car ID и его сохранения
def check_and_save_car_id():
    while True:
        print("\n--- Enter Car ID ---")
        car_id = input("Enter the Car ID (unique): ")

        # Проверка, существует ли файл с сохраненными Car ID
        if os.path.exists("CarsID.txt"):
            with open("CarsID.txt", "r") as f:
                existing_ids = f.read().splitlines()
        else:
            existing_ids = []

        # Проверка, уникален ли введенный Car ID
        if car_id in existing_ids:
            print("Invalid input: This Car ID already exists. Please use a unique ID.")
        else:
            # Сохранение нового уникального Car ID в файл
            with open("CarsID.txt", "a") as f:
                f.write(car_id + "\n")
            print(f"Car ID '{car_id}' saved successfully.")
            return car_id

# Функция для сохранения информации о машине в указанной папке
def save_car_info(folder_name, car_id, car_info):
    # Создаем путь к файлу на основе папки и уникального Car ID
    file_path = os.path.join(folder_name, f"{car_id}.txt")
    
    # Записываем информацию о машине в файл
    with open(file_path, "w") as car_file:
        car_file.write(car_info)
    
    print(f"\nCar information saved in '{file_path}'\n")

# Main function
def main():
    print("Welcome to the Car Dealer App")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new car")
        print("2. View existing cars")
        print("3. Exit")
        print("4. Delete existing file or folder")
        print("5. Edit file")
        print("6. Restore deleted file")
        print("7. Empty bucket")
        print("8. Move files")
        print("9. Search files")
        print("10. Display table")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            folder_name = select_or_create_folder()
            car_id = check_and_save_car_id()
            car_model = input("Enter the Car Model: ")
            car_year = input("Enter the Year of Manufacture: ")
            car_color = input("Enter the Color of the Car: ")
            car_price = input("Enter the Price of the Car: ")

            car_info = f"Car ID: {car_id}\nCar Model: {car_model}\nYear of Manufacture: {car_year}\nColor: {car_color}\nPrice: {car_price}\n"
            save_car_info(folder_name, car_id, car_info)
        
        elif choice == '2':
            view_cars()
        
        elif choice == '3':
            print("\nExiting the application. Goodbye!")
            break
        
        elif choice == '4':
            delete_file()
        
        elif choice == '5':
            edit_file()
        
        elif choice == '6':
            restore_file()

        elif choice == '7':
            empty_bucket()

        elif choice == '8':
            move_file()
  
        elif choice == '9':
            search_files()

        elif choice == '10':
            display_table()
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

