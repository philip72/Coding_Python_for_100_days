from faker import Faker

fake = Faker()

def generate_true_false_question():
    question = fake.sentence()
    answer = fake.random_element(elements=('True', 'False'))
    return question, answer

# Example usage
question, answer = generate_true_false_question()

print("Question:", question)
print("Answer:", answer)
