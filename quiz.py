class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question          # 문제 (str)
        self.choices = choices            # 선택지 (list, 길이 4)
        self.answer = answer              # 정답 (int, 1~4)

    def display(self):
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer