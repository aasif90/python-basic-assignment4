# write_append_file.py

# Step 1: Write user input to output.txt
user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
additional_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display the final content
print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    print(file.read())
