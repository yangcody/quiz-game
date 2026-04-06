\# Quiz Game



\## 1. 프로젝트 개요

Python 콘솔 기반 퀴즈 게임 프로그램

퀴즈 풀고, 새로운 문제 추가, 점수 확인 가능

데이터는 JSON 파일로 저장, 프로그램 재실행 시에도 유지



\## 2. 퀴즈 주제 및 선정 이유

퀴즈 주제는 Python 프로그래밍,

미션2의 내용과 직접 관련된 주제 선정함



\## 3. 실행 방법

Python 설치 및 프로젝트 폴더로 이동하여 다음 명령 실행

python main.py



\## 4. 기능 목록

\- 퀴즈 풀기: 저장된 문제를 순서대로 풀고 점수를 계산

\- 퀴즈 추가: 새로운 문제를 입력하여 저장

\- 퀴즈 목록: 등록된 문제 목록 확인

\- 점수 확인: 최고 점수 조회

\- 데이터 저장: 종료 시 JSON 파일에 자동 저장



\## 5. 파일 구조

quiz-game/

├── main.py          # 프로그램 실행 진입점

├── quiz.py          # Quiz 클래스 정의

├── quiz\_game.py     # QuizGame 클래스 (전체 로직)

├── state.json       # 데이터 저장 파일

├── README.md

└── .gitignore





\## 6. 데이터 파일 설명 (state.json)

\- 종료 후에도 퀴즈 데이터 및 최고 점수 저장하는 역할

&#x20; 퀴즈 한 문제 당 question, choices, answer로 세트 구성,

&#x20;  quizzes 밑에 { }를 퀴즈 수 만큼 작성하고 마지막에 최고 점수를 best\_score에 기록



{

&#x20;   "quizzes": \[

&#x20;       {

&#x20;           "question": "문제",

&#x20;           "choices": \["A", "B", "C", "D"],

&#x20;           "answer": 1

&#x20;       }

&#x20;   ],

&#x20;   "best\_score": 0

}



\## 7. 실행 화면



저장된 데이터 로드. (퀴즈 6개, 최고점수 2점)

========================================

나만의 퀴즈 게임

========================================

1\. 퀴즈 풀기

2\. 퀴즈 추가

3\. 퀴즈 목록

4\. 점수 확인

5\. 종료

========================================

선택:



\## 8. 소스 코드

\### main.py

```python

from quiz\_game import QuizGame



def main():

&#x20;   game = QuizGame()

&#x20;   game.run()



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   main()

```



\### quiz.py

```python
class Quiz:

&#x20;   def \_\_init\_\_(self, question, choices, answer):

&#x20;       self.question = question          # 문제 (str)

&#x20;       self.choices = choices            # 선택지 (list, 길이 4)

&#x20;       self.answer = answer              # 정답 (int, 1\~4)



&#x20;   def display(self):

&#x20;       print(self.question)

&#x20;       print()

&#x20;       for i, choice in enumerate(self.choices, start=1):

&#x20;           print(f"{i}. {choice}")



&#x20;   def check\_answer(self, user\_answer):

&#x20;       return user\_answer == self.answer

```



\### quiz\_game.py

```python

import json

import os

from quiz import Quiz



class QuizGame:

&#x20;   def \_\_init\_\_(self):

&#x20;       self.quizzes = \[]

&#x20;       self.best\_score = 0

&#x20;       self.load\_data()

&#x20;       if not self.quizzes:          # 데이터가 없을 경우

&#x20;           self.load\_default\_quizzes()



&#x20;   def run(self):

&#x20;       try:

&#x20;           while True:

&#x20;               self.show\_menu()

&#x20;               choice = self.get\_user\_input()



&#x20;               if choice == 1:

&#x20;                   self.play\_quiz()

&#x20;               elif choice == 2:

&#x20;                   self.add\_quiz()

&#x20;               elif choice == 3:

&#x20;                   self.list\_quizzes()

&#x20;               elif choice == 4:

&#x20;                   self.show\_score()

&#x20;               elif choice == 5:

&#x20;                   print("퀴즈 종료")

&#x20;                   self.save\_data()

&#x20;                   break

&#x20;       except (KeyboardInterrupt, EOFError):

&#x20;           print("\\n프로그램 중단, 데이터 저장 후 종료")

&#x20;           self.save\_data()

&#x20;       except Exception as e:

&#x20;           print(f"\\n예기치 못한 오류 발생: {e}")

&#x20;           print("데이터 저장 후 종료")

&#x20;           self.save\_data()



&#x20;   def show\_menu(self):

&#x20;       print("=" \* 40)

&#x20;       print("나만의 퀴즈 게임")

&#x20;       print("=" \* 40)

&#x20;       print("1. 퀴즈 풀기")

&#x20;       print("2. 퀴즈 추가")

&#x20;       print("3. 퀴즈 목록")

&#x20;       print("4. 점수 확인")

&#x20;       print("5. 종료")

&#x20;       print("=" \* 40)



&#x20;   def get\_user\_input(self):

&#x20;       while True:

&#x20;           try:

&#x20;               user\_input = input("선택: ").strip()



&#x20;               if not user\_input:              # 빈 입력 처리

&#x20;                   print("빈 입력, 다시.")

&#x20;                   continue



&#x20;               choice = int(user\_input)        # 숫자 변환



&#x20;               if choice < 1 or choice > 5:    # 범위 검증

&#x20;                   print("잘못된 입력, 1-5 사이 숫자 입력")

&#x20;                   continue



&#x20;               return choice



&#x20;           except ValueError:

&#x20;               print("잘못된 입력, 숫자 입력")



&#x20;           except (KeyboardInterrupt, EOFError):

&#x20;               print("\\n퀴즈 게임 종료")

&#x20;               self.save\_data()   # 이후 단계에서 구현됨

&#x20;               exit()



&#x20;   def play\_quiz(self):

&#x20;       if not self.quizzes:

&#x20;           print("등록된 퀴즈가 없습니다.")

&#x20;           return



&#x20;       print("-" \* 40)

&#x20;       print("\\n퀴즈를 시작합니다!")

&#x20;       print(f"(총 {len(self.quizzes)}문제)")

&#x20;       print("-" \* 40)



&#x20;       score = 0



&#x20;       for idx, quizob in enumerate(self.quizzes, start=1):

&#x20;           print(f"\\n\[문제 {idx}]")

&#x20;           quizob.display()



&#x20;           user\_answer = self.get\_answer\_input()



&#x20;           if quizob.check\_answer(user\_answer):

&#x20;               print("정답입니다!")

&#x20;               score += 1

&#x20;           else:

&#x20;               print(f"오답! 정답은 {quizob.answer}번")



&#x20;       print("\\n" + "=" \* 40)

&#x20;       print(f"결과: {len(self.quizzes)}문제 중 {score}문제 정답!( {score/len(self.quizzes)\*100:.0f}점)")



&#x20;       if score > self.best\_score:             # 최고 점수 갱신

&#x20;           print("새로운 최고 점수입니다!")

&#x20;           self.best\_score = score



&#x20;   def get\_answer\_input(self):

&#x20;       while True:

&#x20;           try:

&#x20;               user\_input = input("\\n정답 입력(1\~4): ").strip()



&#x20;               if not user\_input:

&#x20;                   print("빈 입력, 다시 정답 입력")

&#x20;                   continue



&#x20;               answer = int(user\_input)



&#x20;               if answer < 1 or answer > 4:

&#x20;                   print("1\~4 숫자 입력")

&#x20;                   continue



&#x20;               return answer

&#x20;           except ValueError:

&#x20;               print("숫자 입력")

&#x20;           except (KeyboardInterrupt, EOFError):

&#x20;               print("\\n프로그램 종료")

&#x20;               self.save\_data()

&#x20;               exit()



&#x20;   def add\_quiz(self):

&#x20;       print("\\n새로운 퀴즈를 추가합니다.")



&#x20;       try:

&#x20;           question = input("문제를 입력하세요: ").strip()   # 문제 입력

&#x20;           if not question:

&#x20;               print("문제는 비어 있을 수 없습니다.")

&#x20;               return



&#x20;           choices = \[]                                    # 선택지 입력

&#x20;           for i in range(1, 5):

&#x20;               choice = input(f"선택지 {i}: ").strip()

&#x20;               if not choice:

&#x20;                   print("선택지 비어 있음, 다시 입력")

&#x20;                   return

&#x20;               choices.append(choice)



&#x20;           answer = self.get\_answer\_input()                # 정답 입력

&#x20;           new\_quiz = Quiz(question, choices, answer)      # Quiz 객체 생성

&#x20;           self.quizzes.append(new\_quiz)                   # 리스트에 추가

&#x20;           print("퀴즈가 추가되었습니다!")

&#x20;       except (KeyboardInterrupt, EOFError):

&#x20;           print("\\n입력 중단. 프로그램 종료")

&#x20;           self.save\_data()

&#x20;           exit()



&#x20;   def list\_quizzes(self):

&#x20;       if not self.quizzes:

&#x20;           print("\\n등록된 퀴즈 없음\\n")

&#x20;           return



&#x20;       print(f"\\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")

&#x20;       print("-" \* 40)



&#x20;       for idx, quizob in enumerate(self.quizzes, start=1):

&#x20;           print(f"\[{idx}] {quizob.question}")



&#x20;       print("-" \* 40)

&#x20;       print()



&#x20;   def show\_score(self):

&#x20;       print("\\n점수 확인")



&#x20;       if self.best\_score == 0:

&#x20;           print("0점(아직 퀴즈 풀기 전)\\n")

&#x20;           return



&#x20;       total = len(self.quizzes)



&#x20;       print("-" \* 40)

&#x20;       print(f"최고 점수: {self.best\_score/total\*100:.0f}점 ({total}문제 중 {self.best\_score}문제 정답)")

&#x20;       print("-" \* 40)





&#x20;   def load\_data(self):

&#x20;       if not os.path.exists("state.json"):

&#x20;           print("기본 퀴즈 사용")

&#x20;           return



&#x20;       try:

&#x20;           with open("state.json", "r", encoding="utf-8") as fileob:

&#x20;               data = json.load(fileob)



&#x20;           self.quizzes = \[

&#x20;               Quiz(quizfileold\["question"], quizfileold\["choices"], quizfileold\["answer"])

&#x20;               for quizfileold in data.get("quizzes", \[])

&#x20;           ]



&#x20;           self.best\_score = data.get("best\_score", 0)

&#x20;           print(f"저장된 데이터 로드. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best\_score}점)")

&#x20;       except (json.JSONDecodeError, KeyError, TypeError):

&#x20;           print("데이터 파일 손상, 기본 데이터로 복구")

&#x20;           self.load\_default\_quizzes()

&#x20;           self.best\_score = 0

&#x20;       except Exception as e:

&#x20;           print(f"데이터 로드 중 오류 발생: {e}")



&#x20;   def save\_data(self):

&#x20;       data = {

&#x20;           "quizzes": \[

&#x20;               {

&#x20;                   "question": quizob.question,

&#x20;                   "choices": quizob.choices,

&#x20;                   "answer": quizob.answer

&#x20;               }

&#x20;               for quizob in self.quizzes

&#x20;           ],

&#x20;           "best\_score": self.best\_score

&#x20;       }



&#x20;       try:

&#x20;           with open("state.json", "w", encoding="utf-8") as fileob:

&#x20;               json.dump(data, fileob, ensure\_ascii=False, indent=4)

&#x20;       except Exception as e:

&#x20;           print(f"데이터 저장 중 오류 발생: {e}")





&#x20;   def load\_default\_quizzes(self):

&#x20;       self.quizzes = \[

&#x20;           Quiz(

&#x20;               "Python의 창시자는?",

&#x20;               \["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"],

&#x20;               2

&#x20;           ),

&#x20;           Quiz(

&#x20;               "Python의 파일 확장자는?",

&#x20;               \[".java", ".py", ".cpp", ".js"],

&#x20;               2

&#x20;           ),

&#x20;           Quiz(

&#x20;               "리스트(List)의 특징으로 맞는 것은?",

&#x20;               \["순서 없음", "변경 불가", "중복 허용", "키-값 구조"],

&#x20;               3

&#x20;           ),

&#x20;           Quiz(

&#x20;               "딕셔너리(dict)의 특징은?",

&#x20;               \["순서 없음", "키-값 쌍", "중복 허용 안됨", "숫자만 저장"],

&#x20;               2

&#x20;           ),

&#x20;           Quiz(

&#x20;               "True 또는 False 값을 가지는 타입은?",

&#x20;               \["int", "str", "bool", "list"],

&#x20;               3

&#x20;           )

&#x20;       ]

```



