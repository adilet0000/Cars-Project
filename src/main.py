from car_utils import select_or_create_folder, check_and_save_car_id, save_car_info
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
