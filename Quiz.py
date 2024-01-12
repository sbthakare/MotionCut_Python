import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        random.shuffle(self.questions)
        
        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question['text']}")
            self.display_options(question['options'])
            
            user_answer = self.get_user_input()
            if self.check_answer(question, user_answer):
                print("Correct! Well done.")
                self.score += 1
            else:
                print(f"Sorry, the correct answer is: {question['answer']}")
        
        self.display_final_score()

    def display_options(self, options):
        for key, value in options.items():
            print(f"{key}. {value}")

    def get_user_input(self):
        user_input = input("\nSelect Option: ").upper()
      
        return user_input

    def check_answer(self, question, user_answer):
        return user_answer == question['answer']

    def display_final_score(self):
        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")



if __name__ == "__main__":
    quiz_questions = [
        {
            'text': 'Who developed the Python language??',
            'options': {'A': 'Zim Den', 'B': 'Guido van Rossum', 'C': 'Niene Stom','D':'Wick van Rossum'},
            'answer': 'B'
        },
        {
           'text': 'In which year was the Python language developed?',
            'options': {'A': '1995', 'B': '1972', 'C': '1981','D':'1989'},
            'answer': 'D'
        },
        {
           'text': 'Which one of the following is the correct extension of the Python file?',
            'options': {'A': '.py', 'B': '.python', 'C': '.java','D':'.c'},
            'answer': 'A'
        },
        {
           'text': 'Which character is used in Python to make a single line comment?',
            'options': {'A': '/', 'B': '#', 'C': '//','D':'!'},
            'answer': 'B'
        },
        {
           'text': 'Which one of the following has the highest precedence in the expression? ',
            'options': {'A': 'Division', 'B': 'Subtraction', 'C': 'Parentheses','D':'power'},
            'answer': 'C'
        },
    ]

    quiz_game = QuizGame(quiz_questions)
    quiz_game.run_quiz()
