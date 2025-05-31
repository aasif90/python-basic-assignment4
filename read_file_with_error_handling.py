# read_file_with_error_handling.py

# Try to open and read sample.txt
try:
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: sample.txt not found.")
