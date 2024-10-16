import os
import shutil

def view_cars():
    base_dir = "car_data"
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    if not folders:
        print("No car brands available.")
        return

    print("\nAvailable Car Brands and Models:")
    for folder in folders:
        print(f"\nBrand: {folder}")
        files = [f for f in os.listdir(os.path.join(base_dir, folder)) if f.endswith('.txt')]
        for file in files:
            print(f"  Model: {file.replace('.txt', '')}")

def edit_file():
    view_cars()  # Функция, которая отображает список доступных машин
    base_dir = "car_data"

    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    print("\nAvailable brand folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    
    # Добавляем возможность возврата в главное меню
    folder_choice = input("\nEnter the number of the brand folder to edit a file in (or 0 to go back): ")
    if folder_choice == '0':
        return
    
    folder_choice = int(folder_choice) - 1
    folder_path = os.path.join(base_dir, folders[folder_choice])

    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

        print("\nAvailable files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        # Добавляем возможность возврата в главное меню
        file_choice = input("\nEnter the number of the file you want to edit (or 0 to go back): ")
        if file_choice == '0':
            return

        file_choice = int(file_choice) - 1
        file_path = os.path.join(folder_path, files[file_choice])

        if os.path.exists(file_path):
            with open(file_path, "r+") as f:
                lines = f.readlines()
                print("\nCurrent file contents:")

                for i, line in enumerate(lines, start=1):
                    print(f"{i}. {line.strip()}")

                # Добавляем возможность возврата в главное меню
                line_choice = input("\nEnter the number of the line you want to edit (or 0 to go back): ")
                if line_choice == '0':
                    return

                line_choice = int(line_choice) - 1
                current_content = lines[line_choice].strip()

                print(f"\nCurrent content: {current_content}")
                new_content = input("Enter the new content: ")

                lines[line_choice] = new_content + '\n'

                f.seek(0)
                f.writelines(lines)
                f.truncate()

            print(f"\nFile '{files[file_choice]}' updated.")
        else:
            print("File does not exist.")
    else:
        print("Folder does not exist.")


def delete_file():
    view_cars()
    base_dir = "car_data"
    
    folder_choice = input("\nEnter the brand folder name to delete a file from (or 0 to go back): ")
    if folder_choice == '0':
        return

    folder_path = os.path.join(base_dir, folder_choice)
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        
        file_choice = input("\nEnter the file name you want to delete (or 0 to go back): ")
        if file_choice == '0':
            return

        file_path = os.path.join(folder_path, file_choice)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_choice}' deleted.")
        else:
            print("File does not exist.")
    else:
        print("Folder does not exist.")


def move_file():
    base_dir = "car_data"
    
    all_brands = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    if not all_brands:
        print("No car data available.")
        return
    
    print("\nAvailable brand folders:")
    for i, brand in enumerate(all_brands, start=1):
        print(f"{i}. {brand}")
    
    src_choice = input("\nEnter the number of the brand folder to move a file from (or 0 to go back): ")
    if src_choice == '0':
        return

    src_choice = int(src_choice) - 1
    src_folder = os.path.join(base_dir, all_brands[src_choice])

    files = [f for f in os.listdir(src_folder) if f.endswith('.txt')]

    if not files:
        print("No files found in the selected folder.")
        return
    
    print("\nAvailable files to move:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")
    
    file_choice = input("\nEnter the number of the file you want to move (or 0 to go back): ")
    if file_choice == '0':
        return

    file_choice = int(file_choice) - 1
    file_to_move = files[file_choice]

    print("\nAvailable destination folders:")
    for i, brand in enumerate(all_brands, start=1):
        print(f"{i}. {brand}")
    
    dest_choice = input("\nEnter the number of the destination brand folder (or 0 to go back): ")
    if dest_choice == '0':
        return

    dest_choice = int(dest_choice) - 1
    dest_folder = os.path.join(base_dir, all_brands[dest_choice])
    
    shutil.move(os.path.join(src_folder, file_to_move), os.path.join(dest_folder, file_to_move))
    print(f"File '{file_to_move}' moved to '{all_brands[dest_choice]}'.")
