import os


file = "./to_delete_file"

try:
    os.remove(file)
    print("File deleted")
except FileNotFoundError:
    print("File does not exist")
