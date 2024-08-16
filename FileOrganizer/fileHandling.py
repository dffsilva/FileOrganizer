import os
import shutil
from pathlib import Path
import sys

def change_directory(path):
    """Change the current working directory."""
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {path}")
    except Exception as e:
        print(f"Error changing directory: {e}")

# This example changes filenames from
# 'dictionary - python-course-3.mov'
# to --> 
# '03-python-course-dictionary.mov'
def rename_files_in_directory():
    """Rename files in the current directory based on a specific pattern."""
    for file in os.listdir():
        if os.path.isfile(file):  # Ensure it's a file
            name, ext = os.path.splitext(file)
            splitted = [s.strip() for s in name.split("-")]
            if len(splitted) == 4:
                new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"
                os.rename(file, new_name)
                print(f"Renamed: {file} -> {new_name}")
            else:
                print(f"Skipping: {file}, unexpected naming format.")

def create_directory(dir_name):
    """Create a directory if it doesn't exist."""
    Path(dir_name).mkdir(exist_ok=True)
    print(f"Directory '{dir_name}' created or already exists.")

def move_file_or_folder(src, dest):
    """Move a file or folder to a new location."""
    try:
        shutil.move(src, dest)
        print(f"Moved '{src}' to '{dest}'")
    except FileNotFoundError:
        print(f"Source '{src}' not found.")
    except Exception as e:
        print(f"Error moving '{src}': {e}")

def copy_file_or_folder(src, dest):
    """Copy a file or folder to a new location."""
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
        print(f"Copied '{src}' to '{dest}'")
    except FileExistsError:
        print(f"Destination '{dest}' already exists.")
    except FileNotFoundError:
        print(f"Source '{src}' not found.")
    except Exception as e:
        print(f"Error copying '{src}': {e}")

def remove_file_or_folder(target):
    """Remove a file or folder."""
    try:
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
        print(f"Removed '{target}'")
    except FileNotFoundError:
        print(f"Target '{target}' not found.")
    except Exception as e:
        print(f"Error removing '{target}': {e}")

# Example usage
# change_directory("/Users/Diogo Silva/Desktop/videos")
# rename_files_in_directory()
# create_directory("data")
# move_file_or_folder('f', 'd')
# copy_file_or_folder("src", "dest")
# remove_file_or_folder("filename")

def main():
    if len(sys.argv) < 2:
        print("Usage: python fileHandling.py <command> [args]")
        print("Commands: change, rename, create, move, copy, remove")
        return

    command = sys.argv[1].lower()

    if command == "change" and len(sys.argv) == 3:
        change_directory(sys.argv[2])

    elif command == "rename" and len(sys.argv) == 3:
        change_directory(sys.argv[2])
        rename_files_in_directory()

    elif command == "create" and len(sys.argv) == 3:
        create_directory(sys.argv[2])

    elif command == "move" and len(sys.argv) == 4:
        move_file_or_folder(sys.argv[2], sys.argv[3])

    elif command == "copy" and len(sys.argv) == 4:
        copy_file_or_folder(sys.argv[2], sys.argv[3])

    elif command == "remove" and len(sys.argv) == 3:
        remove_file_or_folder(sys.argv[2])

    else:
        print("Invalid command or arguments.")
        print("Usage: python fileHandling.py <command> [args]")
        print("Commands:")
        print("  change <directory_path>")
        print("  rename <directory_path>")
        print("  create <directory_name>")
        print("  move <source> <destination>")
        print("  copy <source> <destination>")
        print("  remove <target>")

if __name__ == "__main__":
    main()