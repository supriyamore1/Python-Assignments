#########################################ASSIGNMENT NO 1 ########################################################################

#1.Using input() function take one number from the user and using ternary operators check whether the number is even or odd
   
  #Solutions: 
  
num = int(input("Enter a number: "))        # Take input from the user
result = "Even" if num % 2 == 0 else "Odd"  # Check if the number is even or odd using a ternary operator
print(f"The number {num} is {result}.")     # Print the result


#2.Using input function take two number and then swap the number 
  
 #Solutions: 

num1 = int(input("Enter the first number: "))             # Take input from the user
num2 = int(input("Enter the second number: "))
print(f"Before swapping: num1 = {num1}, num2 = {num2}")   # Print numbers before swapping
num1, num2 = num2, num1    # Swap the numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")    # Print numbers after swapping


#3.Write a Program to Convert Kilometers to Miles 
  #Solutions: 

conversion_factor = 0.621371                                            # Conversion factor
kilometers = float(input("Enter distance in kilometers: "))             # Take input from the user in kilometers
miles = kilometers * conversion_factor                                  # Convert kilometers to miles
print(f"{kilometers} kilometers is equal to {miles} miles.")            # Print the result


#4.Find the Simple Interest on Rs. 200 for 5 years at 5% per year

  #Solutions: 


P = 200  # Principal amount in Rs.                            # Given values
R = 5    # Rate of interest per year
T = 5    # Time period in years
simple_interest = (P * R * T) / 100                          # Calculate Simple Interest
print(f"The Simple Interest is Rs. {simple_interest}.")      # Print the result

