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

