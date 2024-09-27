#########################################Assignment_no1########################################################################

#1. Write a Python program to sum all the items in a list. 
   
  #Solutions: 
  


numbers = [10, 20, 30, 40, 50]                                                              # Define a list of numbers
total_sum = sum(numbers)                                                                    # Calculate the sum of all items in the list
print("The sum of all items in the list is:", total_sum)                                    # Display the total sum





#2. Write a Python program to get the largest and smallest number from a list without builtin functions.
  
 #Solutions: 


def find_largest_and_smallest(numbers):
    if len(numbers) == 0:                                                                          # Initialize largest and smallest with the first element of the list
        return None, None  # Handle empty list case    
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:                                                                            # Iterate through the list to find the largest and smallest
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest
numbers = [34, 1, 67, -10, 42, 99, 0]                                                              # Example usage
largest, smallest = find_largest_and_smallest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)



#3. Write a Python program to find duplicate values from a list and display those.  
 
  #Solutions: 


def find_duplicates(numbers):
    duplicates = []
    seen = []  # List to keep track of seen numbers
    for num in numbers:
        if num in seen and num not in duplicates:                                                  # If the number has been seen before and is not already in duplicates, add it
            duplicates.append(num)
        else:
            seen.append(num)  # Otherwise, add the number to seen
    return duplicates
numbers = [1, 3, 5, 7, 3, 1, 8, 9, 5]                                                              # Example usage
duplicates = find_duplicates(numbers)
print("Duplicate values:", duplicates)





#4.Write a Python program to split a given list into two parts where the length of the first part of the list is given. Original list: [1, 1, 2, 3, 4, 4, 5, 1]
     #Length of the first part of the list: 3 
     #Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

  #Solutions: 

def split_list(original_list, split_length):
    if split_length > len(original_list):                                                         # Ensure the split length is not greater than the list length
        print("Split length is greater than the list length.")
        return None, None
    first_part = original_list[:split_length]                                                     # Split the list into two parts
    second_part = original_list[split_length:]
    return first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]                                                          # Example usage
split_length = 3  # Length of the first part
first_part, second_part = split_list(original_list, split_length)
print("Original list:", original_list)
print("Length of the first part of the list:", split_length)
print("Splitted the said list into two parts:", (first_part, second_part))






#5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 
      #Original list: ['red', 'green', 'white', 'black'] 
      #Traverse the said list in reverse order: black white green red ” 

     #Solution



   
colors = ['red', 'green', 'white', 'black']                                                                 # Original list


for i in range(len(colors)-1, -1, -1):                                                                  # Traverse the list in reverse order and print each element with its original index
    print(f'Index {i}: {colors[i]}')




###############################################################Assignment no. 2#########################################################################################
#1. Write a Python program and calculate the mean of the below dictionary. 
     #test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} Output: 6.2

    #Solution

def calculate_mean(test_dict):
    total_sum = 0                                                                                      # Get the sum of all values and the total number of values
    count = 0
    for value in test_dict.values():
        total_sum += value
        count += 1
    mean = total_sum / count                                                                            # Calculate the mean
    return mean
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}                                                    # Example usage
mean_value = calculate_mean(test_dict)
print("Mean of the dictionary values:", mean_value)




#2. Write a Python script to concatenate the following dictionaries to create a new one. 
    #Sample Dictionary : 
       #dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
       #Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

    #Solution

def concatenate_dictionaries(dic1, dic2, dic3):
    new_dict = {}                                                                                        # Create a new dictionary by merging dic1, dic2, and dic3    
    for d in (dic1, dic2, dic3):                                                                         # Add all items from each dictionary to the new dictionary
        new_dict.update(d)
    return new_dict
dic1 = {1: 10, 2: 20}                                                                                     # Example usage
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = concatenate_dictionaries(dic1, dic2, dic3)
print("Concatenated dictionary:", result)




#3.Write a Python program to get the key, value and item in a dictionary. 
     #input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
     #Output:
     #key    value
     #1         10
     #2        20
     #3        30
     #4       40
     #5       50
     #6       60 



    #Solution
def print_dict_items(dict_num):
    print(f"{'key':<5}{'value'}")  
    for key, value in dict_num.items():                                                                 # Iterate over the dictionary and print keys and values
        print(f"{key:<5}{value}")
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}                                                   # Example usage
print_dict_items(dict_num)







