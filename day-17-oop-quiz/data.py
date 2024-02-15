from faker import Faker

fake = Faker()

def generate_true_false_question():
    question = fake.sentence()
    answer = fake.random_element(elements=('True', 'False'))
    return question, answer

# Example usage
question, answer = generate_true_false_question()

#print("Question:", question)
# print("Answer:", answer)


def create_question_data():
    my_list=[]
    for i in range(0, 20):
        question, answer = generate_true_false_question()
        my_dict= {'text': question, 'answer': answer}
        my_list.append(my_dict)
        i+=1
    return my_list

# my_list=create_question_data()

# print(my_list)
