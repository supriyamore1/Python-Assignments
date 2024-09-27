#########################################Assignment_no1########################################################################

#1.Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 
   
  #Solutions: 
  


def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
       
read_file_line_by_line('ABC.txt')




#2.Write a function in Python to count and display the total number of words in a text file “ABC.txt”
  
 #Solutions: 


def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

count_words_in_file('ABC.txt')



#3.Write a function in Python to count uppercase character in a text file “ABC.txt”  
 
  #Solutions: 


def count_uppercase_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Call the function
count_uppercase_in_file('ABC.txt')



#4.Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

  #Solutions: 

def display_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                short_words = [word for word in words if len(word) < 4]
                print(" ".join(short_words))
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

display_words('story.txt')



###############################################################Assignment__no__2#########################################################################################

#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 

    #Solution

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
divide_numbers(10, 0)




#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
    
    #Solution

def input_integer():
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Call the function
input_integer()




#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

    #Solution


def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Example usage
open_file('non_existent_file.txt')



#4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

   #Solution


def input_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
            raise TypeError("Both inputs must be numbers.")
        
        num1 = float(num1)
        num2 = float(num2)
        print(f"The sum is: {num1 + num2}")
    except TypeError as e:
        print(f"Error: {e}")

# Call the function
input_numbers()
