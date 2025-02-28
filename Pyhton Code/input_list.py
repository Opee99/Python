# Prompt the user for the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Create an empty list
my_list = []

# Iterate over the range of elements and ask the user to enter each value
for i in range(num_elements):
    value = input(f"Enter the value for element {i+1}: ")
    my_list.append(value)

# Print the final list
print("The list you entered is:", my_list)
