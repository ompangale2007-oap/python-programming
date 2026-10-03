
V = "PYTHON"
vowels = "AEIOUaeiou"
count = 0

for i in range(len(V)):
    if V[i] in vowels:
        count += 1

if count > 0:
    print(f"Number of vowels found are: {count}")
else:
    print("No vowels found")