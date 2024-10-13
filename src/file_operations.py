import os
import shutil
from car_utils import select_or_create_folder

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

    # Получаем список папок брендов
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    # Выводим папки с нумерацией для удобства выбора
    print("\nAvailable brand folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")

    # Выбор папки по номеру
    folder_choice = int(input("\nEnter the number of the brand folder to edit a file in: ")) - 1
    folder_path = os.path.join(base_dir, folders[folder_choice])

    if os.path.exists(folder_path):
        # Получаем список файлов
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        
        # Выводим файлы с нумерацией
        print("\nAvailable files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        # Выбор файла по номеру
        file_choice = int(input("\nEnter the number of the file you want to edit: ")) - 1
        file_path = os.path.join(folder_path, files[file_choice])

        if os.path.exists(file_path):
            with open(file_path, "r+") as f:
                lines = f.readlines()
                print("\nCurrent file contents:")
                
                # Отображаем содержимое файла с нумерацией строк
                for i, line in enumerate(lines, start=1):
                    print(f"{i}. {line.strip()}")

                # Предоставляем выбор строки для редактирования
                line_choice = int(input("\nEnter the number of the line you want to edit: ")) - 1
                current_content = lines[line_choice].strip()

                # Показываем текущее содержимое выбранной строки и предлагаем ввести новое
                print(f"\nCurrent content: {current_content}")
                new_content = input("Enter the new content: ")

                # Заменяем выбранную строку новым содержимым
                lines[line_choice] = new_content + '\n'

                # Перезаписываем файл с новыми данными
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
    folder_choice = input("\nEnter the brand folder name to delete a file from: ")

    folder_path = os.path.join(base_dir, folder_choice)
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        file_choice = input("\nEnter the file name you want to delete: ")

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
    
    # Отображаем все доступные папки брендов
    all_brands = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    if not all_brands:
        print("No car data available.")
        return
    
    # Отображаем папки для выбора источника
    print("\nAvailable brand folders:")
    for i, brand in enumerate(all_brands, start=1):
        print(f"{i}. {brand}")
    
    # Выбор папки-источника
    src_choice = int(input("\nEnter the number of the brand folder to move a file from: ")) - 1
    if src_choice not in range(len(all_brands)):
        print("Invalid choice.")
        return
    src_folder = os.path.join(base_dir, all_brands[src_choice])
    
    # Получаем список файлов в выбранной папке
    files = [f for f in os.listdir(src_folder) if f.endswith('.txt')]
    
    if not files:
        print("No files found in the selected folder.")
        return
    
    # Отображаем файлы для выбора
    print("\nAvailable files to move:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")
    
    # Выбор файла для перемещения
    file_choice = int(input("\nEnter the number of the file you want to move: ")) - 1
    if file_choice not in range(len(files)):
        print("Invalid choice.")
        return
    file_to_move = files[file_choice]
    
    # Отображаем папки для выбора целевой папки
    print("\nAvailable destination folders:")
    for i, brand in enumerate(all_brands, start=1):
        print(f"{i}. {brand}")
    
    # Выбор целевой папки
    dest_choice = int(input("\nEnter the number of the destination brand folder: ")) - 1
    if dest_choice not in range(len(all_brands)):
        print("Invalid choice.")
        return
    dest_folder = os.path.join(base_dir, all_brands[dest_choice])
    
    # Перемещение файла
    shutil.move(os.path.join(src_folder, file_to_move), os.path.join(dest_folder, file_to_move))
    print(f"File '{file_to_move}' moved to '{all_brands[dest_choice]}'.")
