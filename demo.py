# # for val in sequence:
# # loop body

# # for val in sequence:
  

# n= "hello"
# for i in n:
#  print (i)
 
# # The range function is used with a loop to specify how many times the code block
# # will run. 
# for i in range(10): #starts from 0 and execute 10 times
#      print(i)
 
 
#  #input an integer value
# n = int(input("Enter the number whose sum you want to find: "))
# sum=0

# for i in range (1, n+1): #by default range starts from 0 so we defined here start from 1 and execute till n+1 , it means dont include n+1 
#   sum = sum+i 
#   print("\nSum =", sum)
  
#   #if n=5 , n+1 = 6 , so dont include 6 , execute 5 times
  
  
# #   start = n → start from n

# # stop = 0 → stop just before 0 (not inclusive)

# # step = -1 → decrease by 1 each time (counting down)
  
  
  
# #Input a word or sentence
# original = "hello"
# reversed_str = ""

# for char in original:
#     reversed_str = char + reversed_str

# print("Reversed:", reversed_str)





i = 1
while i <= 3:  # Outer loop 
    j = 1
    while j <= 3:  # Inner loop
        print(f"{i}*{j} = {i*j}")
        j += 1 #2
    i += 1
    
  # Get input from user
low = int(input("Enter the lower range: "))
high = int(input("Enter the higher range: "))

prime_count = 0  # To count how many primes found

# Outer loop: check each number in the range
for num in range(low, high + 1):
    if num > 1:  # 0 and 1 are not prime
        is_prime = True
        # Inner loop: check if num is divisible by any number between 2 and num-1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break  # Not prime, no need to check further
        if is_prime:
            prime_count += 1

print(f"Number of prime numbers between {low} and {high} is: {prime_count}")
  
  #Write a program to check how many times a character is repeated in a word?
   
   # Get input from user
word = input("Enter a word: ")

# Dictionary to store character counts
char_count = {}

# Loop through each character in the word
for char in word:
    if char in char_count:
        char_count[char] += 1  # Increment if already in dictionary
    else:
        char_count[char] = 1   # Add new entry

# Display results
print("Character repetitions in the word:")
for char, count in char_count.items():
    print(f"'{char}': {count} time(s)")
 
    



  
