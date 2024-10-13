import os
import shutil

BUCKET_FOLDER = "bucket"
CARS_ID_FILE = "cars.id"  # Файл, где хранятся все ID машин

def ensure_bucket_exists():
    if not os.path.exists(BUCKET_FOLDER):
        os.makedirs(BUCKET_FOLDER)

def load_car_ids():
    """Загружает список машин из файла cars.id"""
    if os.path.exists(CARS_ID_FILE):
        with open(CARS_ID_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_car_ids(car_ids):
    """Сохраняет обновлённый список машин в файл cars.id"""
    with open(CARS_ID_FILE, "w") as f:
        for car_id in car_ids:
            f.write(car_id + "\n")

def delete_file():
    ensure_bucket_exists()

    base_dir = "car_data"
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    print("\nAvailable brand folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")

    # Ввод через цифру, вместо полного названия папки
    folder_choice = int(input("\nEnter the number of the brand folder to delete a file from: ")) - 1
    folder_path = os.path.join(base_dir, folders[folder_choice])

    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

        print("\nAvailable files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        # Ввод через цифру, вместо полного имени файла
        file_choice = int(input("\nEnter the number of the file you want to delete: ")) - 1
        file_path = os.path.join(folder_path, files[file_choice])

        if os.path.exists(file_path):
            # Перемещаем файл в папку bucket
            shutil.move(file_path, os.path.join(BUCKET_FOLDER, files[file_choice]))
            print(f"File '{files[file_choice]}' moved to the bucket.")

            # Удаляем ID машины из cars.id
            car_ids = load_car_ids()
            car_id_to_delete = files[file_choice].replace(".txt", "")  # Предполагается, что ID — это имя файла без расширения
            if car_id_to_delete in car_ids:
                car_ids.remove(car_id_to_delete)
                save_car_ids(car_ids)
                print(f"Car ID '{car_id_to_delete}' removed from '{CARS_ID_FILE}'.")
            else:
                print(f"Car ID '{car_id_to_delete}' not found in '{CARS_ID_FILE}'.")
        else:
            print("File does not exist.")
    else:
        print("Folder does not exist.")


        
def restore_file():
    ensure_bucket_exists()
    
    bucket_files = [f for f in os.listdir(BUCKET_FOLDER) if f.endswith('.txt')]
    if not bucket_files:
        print("No files in the bucket.")
        return

    print("\nFiles in the bucket:")
    for i, file in enumerate(bucket_files, start=1):
        print(f"{i}. {file}")

    # Ввод через цифру, вместо полного имени файла
    file_choice = int(input("\nEnter the number of the file to restore: ")) - 1
    file_name = bucket_files[file_choice]
    file_path = os.path.join(BUCKET_FOLDER, file_name)

    if os.path.exists(file_path):
        dest_folders = [f for f in os.listdir() if os.path.isdir(f)]  # Получаем список всех папок в текущем каталоге

        print("\nAvailable destination folders:")
        for i, folder in enumerate(dest_folders, start=1):
            print(f"{i}. {folder}")

        # Ввод через цифру, вместо полного имени папки
        folder_choice = int(input("\nEnter the number of the destination folder: ")) - 1
        dest_folder = dest_folders[folder_choice]

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        
        # Восстановление файла
        shutil.move(file_path, os.path.join(dest_folder, file_name))
        print(f"File '{file_name}' restored to '{dest_folder}'.")
    else:
        print("File not found in the bucket.")


def empty_bucket():
    ensure_bucket_exists()
    for file in os.listdir(BUCKET_FOLDER):
        file_path = os.path.join(BUCKET_FOLDER, file)
        os.remove(file_path)
    print("Bucket emptied.")
