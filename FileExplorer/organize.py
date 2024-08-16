import os
import shutil
import sys

# Define file type categories and corresponding destination folders
file_categories = {
    "audio": ((".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", 
              ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", 
              ".tta", ".voc", ".wav", ".wma", ".wv"), "audio"),
    "video": ((".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf"), "videos"),
    "image": ((".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif"), "images"),
    "zip": ((".zip", ".rar", ".7z", ".tar", ".gz"), "zips"),  # Category for zips
}

def organize_files(directory_path):
    os.chdir(directory_path)
    
    # Ensure destination directories exist
    base_path = os.path.expanduser("~/Documents")
    folders = ["audio", "video", "images", "screenshots", "zips"]
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    
    for file in os.listdir():
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            
            for category, (extensions, folder) in file_categories.items():
                if file_ext in extensions:
                    # Special case for screenshots
                    if category == "image" and "screenshot" in os.path.splitext(file)[0].lower():
                        destination = os.path.join(base_path, "screenshots")
                    else:
                        destination = os.path.join(base_path, folder)
                    break
            else:
                destination = base_path
            
            # Move the file
            try:
                shutil.move(file_path, destination)
                print(f"Moved {file} to {destination}")
            except Exception as e:
                print(f"Error moving {file}: {e}")

# Main function to accept directory path as an argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organize.py <directory_name>")
    else:
        organize_files("/Users/Diogo Silva/" + sys.argv[1])