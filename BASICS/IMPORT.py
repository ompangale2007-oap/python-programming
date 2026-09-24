
import os
if os.path.exists("Sample.txt"):
    print("File Content:\n")
    with open("Sample.txt", "r") as file:
        for line in file:
            print(line, end="") 
else:
    print(f"Error: The file was not found.")