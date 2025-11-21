import os
import shutil

# ====== Folder to organize ======
# Change this path to any folder you want
FOLDER_PATH = "C:/Users/Public/Downloads"

# ====== File categories ======
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"],
}

# ====== Create folders ======
for folder_name in FILE_TYPES.keys():
    folder_path = os.path.join(FOLDER_PATH, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# ====== Move files ======
moved_files = []

for file_name in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    file_ext = os.path.splitext(file_name)[1].lower()

    for folder_name, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            dest_path = os.path.join(FOLDER_PATH, folder_name, file_name)
            shutil.move(file_path, dest_path)
            moved_files.append((file_name, folder_name))
            break

# ====== Output summary ======
print("\n FILE ORGANIZER RESULTS \n")
if moved_files:
    for f, folder in moved_files:
        print(f" Moved '{f}' → {folder}")
else:
    print("No files were moved — all organized already.")

print("\n Folder organization complete!\n")











