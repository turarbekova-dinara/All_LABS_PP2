import os

def check_path(path):
    return [os.path.exists(path), os.access(path, os.R_OK), os.access(path, os.W_OK), os.access(path, os.X_OK)]

path = "example.txt"
exists, readable, writable, executable = check_path(path)

print(f"Path: {path}")
print(f"Exists: {exists}, Readable: {readable}, Writable: {writable}, Executable: {executable}")
