from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_default_quizzes()   # 여기서 기본 데이터 로드

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_input()

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("프로그램 종료합니다.")
                break

    def show_menu(self):
        print("=" * 40)
        print("\n나만의 퀴즈 게임")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_user_input(self):
        while True:
            try:
                user_input = input("선택: ").strip()

                if not user_input:              # 빈 입력 처리
                    print("빈 입력, 다시.")
                    continue

                choice = int(user_input)        # 숫자 변환

                if choice < 1 or choice > 5:    # 범위 검증
                    print("잘못된 입력, 1-5 사이 숫자 입력")
                    continue

                return choice

            except ValueError:
                print("잘못된 입력, 숫자 입력")

            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈 게임 종료")
                self.save_data()   # 이후 단계에서 구현됨
                exit()

    def play_quiz(self):
        pass

    def add_quiz(self):
        pass

    def list_quizzes(self):
        pass

    def show_score(self):
        pass

    def load_data(self):
        pass

    def save_data(self):
        pass

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
