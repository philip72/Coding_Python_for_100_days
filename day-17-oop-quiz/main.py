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
