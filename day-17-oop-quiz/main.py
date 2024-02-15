class User:
    # init function isto initialize the attrbutes- what objects will have
    def __init__(self,user_id, username): # here they are positional argument
        self.id=user_id #here they are atributes
        self.username=username
        self.followers=0
        self.following=0
    
    def follow(self, user):
        user.followers+=1
        user.following+=1


        

user_1= User(100, 'Phil')
user_2=User(100,"jemy")

user_1.follow(user_2)


print(f'user_1 followers {user_1.followers}')
# pascal case naming case PascalCase

""" tapping into the attribute"""

print(user_1.id)

import data

# question, answer= data.generate_true_false_question()

# my_answer= input('whats your answer').capitalize()

# if my_answer== answer:
#     print('Correct')
# else: 
#     print('wrong')

import question_model
from quiz_brain import QuizBrain
question_data=[]

my_list=data.create_question_data()

for i in my_list:
    question_text= i['text']
    question_answer=i['answer']
    question= question_model.Question(question_text,question_answer)
    question_data.append(question)


quiz= QuizBrain(question_data)

while quiz.still_has_questions():
    quiz.next_question()
print("You have finished the questions")

print(f'Your score is {quiz.score}/{quiz.question_number}')


# print(my_list)

# for i in my_list:
#      for key, value in i.items():
#           print(key, value)

import random 

choosen_random= random.choice(my_list)
print(choosen_random['text'])
print(choosen_random['answer'])

question_test= question_model.Question(choosen_random['text'], choosen_random['answer'])

#print(question_test)

# for i in range(0,1):
#     for key, value in choosen_random.items():
#         print(key, value)
#         i+=1
        
     
