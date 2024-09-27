#########################################Assignment########################################################################

#1.Write a python program to reverse a number using a while loop
   
  #Solutions: 
  

num = int(input("Enter a number: "))                                                     # Take input from the user
reversed_num = 0                                                                         # Initialize variables
temp_num = num
while temp_num > 0:                                                                      # While loop to reverse the number
    remainder = temp_num % 10  # Get the last digit
    reversed_num = (reversed_num * 10) + remainder  # Add it to the reversed number
    temp_num = temp_num // 10  # Remove the last digit from the number
print(f"The reverse of {num} is {reversed_num}.")                                       # Print the reversed number



#2.Write a python program to check whether a number is palindrome or not? 
  
 #Solutions: 


num = int(input("Enter a number: "))                                                 # Take input from the user
original_num = num                                                                   # Store the original number to compare later
reversed_num = 0                                                                     # Initialize reversed number

while num > 0:                                                                       # While loop to reverse the number
    remainder = num % 10  # Get the last digit
    reversed_num = (reversed_num * 10) + remainder  # Form the reversed number
    num = num // 10  # Remove the last digit from the number

if original_num == reversed_num:                                                     # Check if the original number is equal to its reversed version
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")


#3.Write a python program finding the factorial of a given number using a while loop. 
  #Solutions: 


num = int(input("Enter a number to find its factorial: "))               # Take input from the user
factorial = 1                                                            # Initialize variables
counter = 1
while counter <= num:                                                    # While loop to calculate factorial
    factorial *= counter  # Multiply current factorial by the counter
    counter += 1  # Increment the counter
print(f"The factorial of {num} is {factorial}.")                         # Print the result



#4.Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

  #Solutions: 



total_sum = 0                                                       # Initialize sum variable
                                                                    # Infinite loop to accept user inpu
while True:
    number = float(input("Enter a number (0 to stop): "))          # Take input from the user
    if number == 0:                                                # Check if the number is 0
        break  # Exit the loop if 0 is entered
    total_sum += number                                            # Add the number to the total sum
print(f"The sum of all entered numbers is: {total_sum}.")          # Print the result


###############################################################Assignment###########################################################################

#1.Print the first 10 natural numbers using for loop

     #Solution


for num in range(1, 11):                                          #range(1, 11) generates numbers from 1 to 10
    print(num)


#2.Python program to check if the given string is a palindrome

    #Solution


import re
def is_palindrome(s):                                                          # Function to check if the string is a palindrome
    
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    return cleaned_string == cleaned_string[::-1]                              # Check if the cleaned string is equal to its reverse
input_string = input("Enter a string: ")                                       # Take input from the user
if is_palindrome(input_string):                                                # Check if the string is a palindrome
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


#3.Python program to check if a given number is an Armstrong number

    #Solution

def is_armstrong_number(num):                                            # Function to check if a number is an Armstrong number
    num_str = str(num)                                                   # Convert the number to string to iterate over digits
    num_digits = len(num_str)  # Count the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)   # Calculate sum of powers  
    return sum_of_powers == num                                          # Check if the sum of powers is equal to the original number
number = int(input("Enter a number: "))                                 # Take input from the user
if is_armstrong_number(number):                                         # Check if the number is an Armstrong number
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


#4.Python program to get the Fibonacci series between 0 to 50

    #Solution


def fibonacci_series(limit):                               # Function to generate Fibonacci series
    fib_series = []
    a, b = 0, 1                                            # Starting values    
    while a <= limit:                                      # Generate Fibonacci numbers until the limit
        fib_series.append(a)
        a, b = b, a + b  # Update values
    return fib_series
limit = 50                                                 # Define the limit
fibonacci_numbers = fibonacci_series(limit)                 # Get the Fibonacci series
print("Fibonacci series between 0 and 50:")
print(fibonacci_numbers)



#5.Python program to check the validity of password input by user

    #Solution


import re
def is_valid_password(password):                                                              # Function to check the validity of a password   
    if len(password) < 8:                                                                     # Check for length
        return False
    if (not re.search(r"[a-z]", password) or                                                  # Check for uppercase, lowercase, digit, and special character
        not re.search(r"[A-Z]", password) or  
        not re.search(r"[0-9]", password) or                                               
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):  
        return False    
    return True
user_password = input("Enter a password to check its validity: ")


if is_valid_password(user_password):                                                          # Check if the password is valid
    print("The password is valid.")
else:
    print("The password is invalid. Please follow these rules:")
    print("- At least 8 characters long")
    print("- Contains both uppercase and lowercase characters")
    print("- Contains at least one numeric digit")
    print("- Contains at least one special character (e.g., @, #, $, etc.)")



