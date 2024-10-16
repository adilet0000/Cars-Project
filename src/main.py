from car_utils import select_or_create_folder, add_car_to_folder, save_car_info
from file_operations import view_cars, edit_file, delete_file, move_file
from bucket_operations import restore_file, empty_bucket
from table_operations import display_table
from search_operations import search_files

def main():
    print("Welcome to the Car Dealer App")

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new car")
        print("2. View existing cars")
        print("3. Delete existing file or folder")
        print("4. Edit file")
        print("5. Restore deleted file")
        print("6. Empty bucket")
        print("7. Move files")
        print("8. Search files")
        print("9. Display table")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            folder_name = select_or_create_folder()
            if folder_name == '0':  # Проверяем, если вернулись в главное меню
                continue
            
            # Добавляем машину в выбранную папку
            add_car_to_folder(folder_name)

        elif choice == '2':
            view_cars()

        elif choice == '3':
            delete_file()

        elif choice == '4':
            edit_file()

        elif choice == '5':
            restore_file()

        elif choice == '6':
            empty_bucket()

        elif choice == '7':
            move_file()

        elif choice == '8':
            search_files()

        elif choice == '9':
            display_table()

        elif choice == '0':
            print("\nExiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
