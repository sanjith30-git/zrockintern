# Function to check if a dictionary is empty
def check_if_dict_empty(d):
    return len(d) == 0

# Taking input from the user
user_dict = {}

# Checking if the dictionary is empty
if check_if_dict_empty(user_dict):
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")
