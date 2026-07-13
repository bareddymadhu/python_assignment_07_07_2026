# patterns.py
# Program to print different patterns using nested loops.

# Get input from the user
size = int(input("Enter the size/height: "))

# --------------------------------------------------
# 1. Square Pattern
# --------------------------------------------------
print("\nSquare Pattern:")
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()

# --------------------------------------------------
# 2. Right-Angled Triangle Pattern (Numbers)
# --------------------------------------------------
print("\nRight-Angled Triangle Pattern:")
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# --------------------------------------------------
# 3. Pyramid Pattern
# --------------------------------------------------
print("\nPyramid Pattern:")
for i in range(size):
    # Print leading spaces
    for j in range(size - i - 1):
        print(" ", end="")
    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")
    print()
