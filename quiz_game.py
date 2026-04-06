from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_default_quizzes()   # 여기서 기본 데이터 로드

    def load_default_quizzes(self):
        self.quizzes = [
            Quiz(
                "Python의 창시자는?",
                ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"],
                1
            ),
            Quiz(
                "Python의 파일 확장자는?",
                [".java", ".py", ".cpp", ".js"],
                2
            ),
            Quiz(
                "리스트(List)의 특징으로 맞는 것은?",
                ["순서 없음", "변경 불가", "중복 허용", "키-값 구조"],
                3
            ),
            Quiz(
                "딕셔너리(dict)의 특징은?",
                ["순서 없음", "키-값 쌍", "중복 허용 안됨", "숫자만 저장"],
                2
            ),
            Quiz(
                "True 또는 False 값을 가지는 타입은?",
                ["int", "str", "bool", "list"],
                3
            )
        ]
