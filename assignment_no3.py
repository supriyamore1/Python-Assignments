#########################################Assignment_no1########################################################################

#1.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 
   
  #Solutions: 
  

def div(a, b):                                       # Define the div() function
    return a / b
result = div(10, 2)                                  # Call the function with two numbers
print("The result of the division is:", result)      # Display the result




#2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number.
  
 #Solutions: 



def square(num):                                         # Define the square() function
    return num * num
result = square(5)                                       # Call the function with one number
print("The square of the number is:", result)            # Display the result


#3.Using max() and min() functions display the maximum and minimum of 5 random numbers. 
 
  #Solutions: 


import random
random_numbers = [random.randint(1, 100) for _ in range(5)]                # Generate 5 random numbers
print("Random numbers:", random_numbers)                                   # Display the random numbers
max_number = max(random_numbers)                                           # Find and display the maximum and minimum of the random numbers
min_number = min(random_numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)




#4.Accept a name from the user and display that in lower case using lower() function 

  #Solutions: 


name = input("Enter your name: ")                          # Accept a name from the user
lowercase_name = name.lower()                              # Display the name in lowercase\
print("Your name in lowercase is:", lowercase_name)



###############################################################Assignment_no2###########################################################################

#1.Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery” 

     #Solution



string = "To change the overall look of your document. To change the look available in the gallery"         # Given sentence
words = string.lower().split()                                                                              # Convert the sentence to lowercase and split it into words
word_count = {}                                                                                             # Initialize an empty dictionary to store word counts
for word in words:                                                                                          # Count the occurrences of each word
    word = word.strip(".")  # Remove punctuation if needed
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():                                                                       # Display the word count
    print(f"'{word}': {count}")



#2. Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n"

    #Solution


string = "\nBest \nDeeptech \nPython \nTraining\n"                                                           # Given string with newlines
cleaned_string = string.replace("\n", " ")                                                                   # Remove the newline characters
print("String without newlines:", cleaned_string)                                                            # Display the cleaned string



#3. Write a Python program to reverse words in a string String = “Deeptech Python Training” 

    #Solution


string = "Deeptech Python Training"                                                                       # Given string
reversed_words = string.split()[::-1]                                                                     # Split the string into words and reverse the list of words
reversed_string = " ".join(reversed_words)                                                                # Join the reversed list of words back into a string
print("Reversed words string:", reversed_string)                                                          # Display the reversed string



#4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training” 



    #Solution



string = "Welcome to python Training"                                                                     # Given string
vowels = "aeiouAEIOU"                                                                                     # Define the vowels
vowel_count = 0                                                                                           # Initialize a counter for vowels
vowel_list = []                                                                                           # List to store the vowels found in the string
for char in string:                                                                                       # Iterate through the string and check for vowels
    if char in vowels:
        vowel_count += 1
        vowel_list.append(char)                                                   
print(f"Number of vowels: {vowel_count}")                                                                 # Display the count and the vowels
print("Vowels found:", " ".join(vowel_list))





