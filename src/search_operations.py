import os

def search_files():
    base_dir = "car_data"
    search_term = input("Enter the term to search for: ").lower()
    
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    for folder in folders:
        files = [f for f in os.listdir(os.path.join(base_dir, folder)) if f.endswith('.txt')]
        for file in files:
            file_path = os.path.join(base_dir, folder, file)
            with open(file_path, "r") as f:
                contents = f.read().lower()
                if search_term in contents:
                    print(f"Match found in file: {file_path}")
