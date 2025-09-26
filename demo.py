# for val in sequence:
# loop body

# for val in sequence:
  

n= "hello"
for i in n:
 print (i)
 
# The range function is used with a loop to specify how many times the code block
# will run. 
for i in range(10): #starts from 0 and execute 10 times
     print(i)
 
 
 #input an integer value
n = int(input("Enter the number whose sum you want to find: "))
sum=0

for i in range (1, n+1): #by default range starts from 0 so we defined here start from 1 and execute till n+1 , it means dont include n+1 
  sum = sum+i 
  print("\nSum =", sum)
  
  #if n=5 , n+1 = 6 , so dont include 6 , execute 5 times
  
  
#   start = n → start from n

# stop = 0 → stop just before 0 (not inclusive)

# step = -1 → decrease by 1 each time (counting down)
  
  
  
#Input a word or sentence
original = "hello"
reversed_str = ""

for char in original:
    reversed_str = char + reversed_str

print("Reversed:", reversed_str)



  
