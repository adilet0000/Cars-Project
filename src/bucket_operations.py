import os
import shutil

BUCKET_FOLDER = "bucket"

def ensure_bucket_exists():
    if not os.path.exists(BUCKET_FOLDER):
        os.makedirs(BUCKET_FOLDER)

def restore_file():
    ensure_bucket_exists()
    bucket_files = [f for f in os.listdir(BUCKET_FOLDER) if f.endswith('.txt')]
    if not bucket_files:
        print("No files in the bucket.")
        return

    print("\nFiles in the bucket:")
    for i, file in enumerate(bucket_files, start=1):
        print(f"{i}. {file}")

    file_choice = input("\nEnter the file name to restore: ")
    file_path = os.path.join(BUCKET_FOLDER, file_choice)
    if os.path.exists(file_path):
        dest_folder = input("\nEnter the destination folder name to restore the file: ")
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        shutil.move(file_path, os.path.join(dest_folder, file_choice))
        print(f"File '{file_choice}' restored to '{dest_folder}'.")
    else:
        print("File not found in the bucket.")

def empty_bucket():
    ensure_bucket_exists()
    for file in os.listdir(BUCKET_FOLDER):
        file_path = os.path.join(BUCKET_FOLDER, file)
        os.remove(file_path)
    print("Bucket emptied.")
