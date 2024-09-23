def convert_to_title_case(string):   # Function to convert a string to title case
    return string.title()      
user_string = input("Enter a string: ")  # Taking input from the user
title_case_string = convert_to_title_case(user_string)  # Converting to title case
print("Title Case String:", title_case_string)  # Displaying the result
