# Ask the user for the number of rows
rows = int(input("Enter the number of rows for the triangle: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print i stars for the current row
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row
    print()
    
    
# Get input from the user
n = int(input("Enter the number of rows for the diamond pattern: "))

# Upper half of the diamond
for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()  # Move to the next line

# Lower half of the diamond
for i in range(n - 1, 0, -1):
    # Print spaces
    print(" " * (n - i), end="")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()  # Move to the next line
  
 
 
 
 
 
 
 
    
# Ask the user for number of rows
rows = int(input("Enter the number of rows for Floyd's Triangle: "))

# Initialize the first number
num = 1

print("\nFloyd's Triangle:")
for i in range(1, rows + 1):      # Loop through rows
    for j in range(1, i + 1):     # Loop to print numbers in each row
        print(num, end=' ')
        num += 1                  # Increment the number
    print()                       # Move to the next line after each row

