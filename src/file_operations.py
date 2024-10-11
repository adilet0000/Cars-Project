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
    view_cars()
    base_dir = "car_data"
    folder_choice = input("\nEnter the brand folder name to edit a file in: ")

    folder_path = os.path.join(base_dir, folder_choice)
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        file_choice = input("\nEnter the file name you want to edit: ")

        file_path = os.path.join(folder_path, file_choice)
        if os.path.exists(file_path):
            with open(file_path, "r+") as f:
                print("\nCurrent file contents:")
                print(f.read())
                f.seek(0)
                new_content = input("\nEnter the new content: ")
                f.write(new_content)
                f.truncate()
            print(f"File '{file_choice}' updated.")
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
    view_cars()
    base_dir = "car_data"
    folder_choice_src = input("\nEnter the brand folder name to move a file from: ")

    src_folder = os.path.join(base_dir, folder_choice_src)
    if os.path.exists(src_folder):
        files = [f for f in os.listdir(src_folder) if f.endswith('.txt')]
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        file_choice = input("\nEnter the file name you want to move: ")

        folder_choice_dest = input("\nEnter the destination brand folder name: ")
        dest_folder = os.path.join(base_dir, folder_choice_dest)
        if os.path.exists(dest_folder):
            shutil.move(os.path.join(src_folder, file_choice), os.path.join(dest_folder, file_choice))
            print(f"File '{file_choice}' moved to '{folder_choice_dest}'.")
        else:
            print("Destination folder does not exist.")
    else:
        print("Source folder does not exist.")
