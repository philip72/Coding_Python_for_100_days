# Example nested list with dictionaries
# Example nested list with dictionaries
nested_list = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 22}
]

# Function to compare the 'age' key in dictionaries within a nested list
def compare_age(nested_list):
    # Assume all entries have the 'age' key
    for i in range(len(nested_list) - 1):
        age1 = nested_list[i]['age']
        age2 = nested_list[i + 1]['age']

        # Compare the 'age' values
        if age1 == age2:
            print(f"Age is equal: {age1}")
        else:
            print(f"Age is not equal: {age1} and {age2}")

# Example usage
compare_age(nested_list)

# Example nested list with dictionaries
nested_list = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 22},
    {'name': 'Eva', 'age': 35}
]

# Function to find and compare the dictionary with the highest 'age'
def compare_and_replace_highest_age(nested_list):
    highest_age_dict = None
    for dictionary in nested_list:
        if highest_age_dict is None or dictionary['age'] > highest_age_dict['age']:
            highest_age_dict = dictionary

    print(f"Dictionary with the highest age: {highest_age_dict}")

    # Now, let's compare with another dictionary
    new_dictionary = {'name': 'Charlie', 'age': 28}

    if new_dictionary['age'] > highest_age_dict['age']:
        print(f"The new dictionary has a higher age, replacing the previous one.")
        highest_age_dict = new_dictionary
    else:
        print("The new dictionary does not have a higher age than the stored one.")

    print(f"Updated dictionary with the highest age: {highest_age_dict}")

# Example usage
compare_and_replace_highest_age(nested_list)


   


