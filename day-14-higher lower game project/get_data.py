from faker import Faker
import random

fake = Faker()

def generate_random_person():
    return {
        'name': fake.name(),
        'follower_count': random.randint(100, 500),
        'description': fake.job(),
        'country': fake.country()
    }

# Generating random data for three people
person1 = generate_random_person()
person2 = generate_random_person()
person3 = generate_random_person()

# Printing the generated data
# print(person1)
# print(person2)
# print(person3)

# Creating a nested list with dictionaries
nested_list_with_faker = [generate_random_person() for _ in range(100)]

# Displaying the nested list
# for person in nested_list_with_faker:
#      print(person)
# print(nested_list_with_faker)