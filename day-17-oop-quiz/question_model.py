class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self) -> str:
        return f'the text is {self.text} and answer is {self.answer}'    

