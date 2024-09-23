# Function to find the maximum number in an array
def find_max_in_array(arr):
    if not arr:  # Check if the array is empty
        return None
    return max(arr)

# Taking input from the user
array = list(map(int, input("Enter numbers separated by space: ").split()))

# Finding the maximum number
max_number = find_max_in_array(array)

# Displaying the result
if max_number is not None:
    print("The maximum number in the array is:", max_number)
else:
    print("The array is empty.")
