# Quiz Game

## 1. 프로젝트 개요

Python 콘솔 기반 퀴즈 게임 프로그램

- 퀴즈 풀고, 새로운 문제 추가, 점수 확인 가능
- 데이터는 JSON 파일로 저장, 프로그램 재실행 시에도 유지

github 링크
```
https://github.com/yangcody/quiz-game
```

## 2. 퀴즈 주제 및 선정 이유

- 퀴즈 주제는 Python 프로그래밍,
- 미션2의 내용과 직접 관련된 주제 선정함

## 3. 실행 방법

- Python 설치 및 프로젝트 폴더로 이동하여 다음 명령 실행
```bash
python main.py
```

## 4. 기능 목록

### 퀴즈 게임 기능

- 퀴즈 풀기: 저장된 문제를 순서대로 풀고 점수를 계산
- 퀴즈 추가: 새로운 문제를 입력하여 저장
- 퀴즈 목록: 등록된 문제 목록 확인
- 점수 확인: 최고 점수 조회
- 데이터 저장: 종료 시 JSON 파일에 자동 저장

### 그래프 결과 및 브랜치 분리/병합 의미
- branch는 현재 코드 상태에서 분리 기록되는 별도의 작업 공간으로 기본은 main
- 기존 main 코드를 안정적으로 유지하는 상태에서 새로운 기능 개발에 사용
- 효과적인 버전관리와 함께 여러명이 동시에 작업할때 상호 충돌 방지 가능
- feature/play-quiz 브랜치 생성하여 checkout
```bash
git checkout -b feature/play-quiz
```

- 프로그램 개발 완료 후 브랜치에서 commit
```bash
git commit -m "Feat: 퀴즈 풀기 기능 구현 (정답 처리 및 점수 계산)"
git push origin feature/play-quiz
```

- main 브랜치로 병합
```bash
git checkout main
git merge feature/play-quiz
git push
```

- 그래프 결과 실행
```bash
$ git log --oneline --graph
* 2328240 (HEAD -> main, origin/main, origin/HEAD) Docs : clone 환경에서 README 수정
* 22cde04 Docs: README 수정8
* 88a8a81 Docs: README 수정7
* 40fa8ef Docs: README 수정6
* 853b5c4 Docs: README 수정5
* 8488864 Docs: README 수정4
* ef19a74 Docs: README 수정3
* 949a2fb Docs: README 재수정
* 5758efd Docs: README 수정 및 소스 코드 추가
* 9d00c9a Docs: README 작성
* 7cc614f Test: 테스트 및 버그 수정
* 280cc8e Feat: JSON 파일 저장 및 불러오기 기능 구현
* 2298ac9 Feat: 최고 점수 조회 기능 구현
* f52947d Feat: 퀴즈 목록 조회 기능 구현
* a9c9e31 Feat: 퀴즈 추가 기능 구현 (입력 처리 및 객체 생성)
* ae1d2a1 (origin/feature/play-quiz, feature/play-quiz) Feat: 퀴즈 풀기 기능 구현 (정답 처리 및 점수 계산)
* 334add1 Feat: 메뉴 입력 검증 및 예외 처리 구현
* 5ff515a Feat: 기본 퀴즈 데이터 5개 추가
* c44a61e Feat: 프로젝트 구조 및 클래스 뼈대 설계
```

- 커밋은 기능 단위로 분리하면서 의미 관련 메시지에 따라 분리,
  "최고 점수 조회 기능 구현", "퀴즈 추가 기능 구현" 등은 기능 단위로 분리하여 "Feat:"로 표시,
  "테스트 및 버그"은 "Test:", README.md 작성은 "Docs:"로 분리하여 표시


## 5. 파일 구조

```
quiz-game/

├── main.py          # 프로그램 실행 진입점

├── quiz.py          # Quiz 클래스 정의

├── quiz_game.py     # QuizGame 클래스 (전체 로직)

├── state.json       # 데이터 저장 파일

├── README.md

└── .gitignore
```


## 6. 데이터 파일 설명 (state.json)

### JSON 특징
- 구조화된 Data 저장에 적합한 형태로서 Python과의 호환성이 높음
- 구현이 단순하고 사람에게 가독성이 높음
- 파일 기반으로 저장하므로 프로그램 재실행 시 데이터 유지
- 대규모 처리나 저장에는 부적합하나 이번 퀴즈게임 미션에는 적합한 수준
- JSON으로 대용량 데이터를 처리하면 성능이 저하되고, 여러 사용자가 동시에 접근하면 충돌 발생하며,검색/필터 등 기능이 부족하여 불편

### 본 미션에서 역할
- 종료 후에도 퀴즈 데이터 및 최고 점수 저장하는 역할
- 퀴즈 한 문제 당 question, choices, answer로 세트 구성,
- quizzes 밑에 { }를 퀴즈 수 만큼 작성하고 마지막에 최고 점수를 best_score에 기록
- state.json을 최초 프로그램이 실행될 때 한번 읽고 "main()에서 QuizGame() 부르고 load_data()", 
  실행 중 data는 메모리에서만 변경되다가, 
  사용자가 5번 퀴즈 종료를 입력하거나 Exception 종료할 때만 한번 쓰는 과정으로 발생 "save_data()"

```json
{

   "quizzes": [
       {
           "question": "문제",
           "choices": ["A", "B", "C", "D"],
           "answer": 1
       }
   ],
   "best_score": 0
}
```



## 7. 실행 화면

```
저장된 데이터 로드. (퀴즈 6개, 최고점수 2점)
========================================
나만의 퀴즈 게임
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택:
```

## 8. Git Clone 실습
PC에서 작업한 Gibhub를 mac에 Clone 후 수정한 내용 반영 추가
```bash
git clone https://gibhub.com/yangcody/quiz-game.git
cd quiz-game
```
mac에서 README.md 파일 수정 후 Github 반영
```bash
git add .
git commit -m "Docs : clone 환경에서 README 수정"
git push
```
원래 PC에서 pull 확인 완료
```bash
git pull
```

## 9. 소스 코드 및 설명

### 함수와 클래스 차이
- 함수는 독립적으로 각 호출마다 단일 기능 실행 후 종료되나,
- 클래스를 실행하면 서로 다른 객체를 유지하고 데이터와 기능을 하나로 묶어서 캡슐화하여 현실세계 모델링 가능하며 결과적으로 소스 코드의 재사용성과 확장성을 높여줌

### 클래스 책임 분리 및 로직 분리
- class Quiz는 퀴즈문제 출력과 정답 체크 기능 수행
  class QuizGame은 사용자 입력 처리와 점수 계산 기능 수행
- 입력 처리(검증)은 사용자 입력을 프로그램 내 값으로 변환하면서 잘못된 입력 차단하는 로직만 구현,
  게임 진행은 프로그램 실제 동작을 수행하여 퀴즈 출제, 점수 계산, 메뉴 흐름에 대한 로직만 구현하고 데이터 보관,
  저장/불러오기는 외부 저장소 JSON을 읽는 기능과 쓰는 기능만 구현하면서 파일 입출력 오류 처리에 집중,
  결과적으로 전체 과정에서 각 공통적인 로직을 분리하여 재사용하도록 하면서, 각 기능 간 불필요한 영향 최소화 
  
### try/except
- 파일 입출력 연산은 외부 환경에 의존하므로 불확실성이 높음
- 파일이 존재하지 않거나, 경로가 잚못 되었거나, 접근 권한이 없거나, 내용이 손상되었을 수 있음
- 이런 상황에서 자동 종료되므로 프로그램의 안정성 확보와 함께 종료 사유를 알려주기 위해 try/except 구조로 프로그램을 짜야 함

### 유지보수 설명
- main.py 파일에서 main() 내부는 특별히 수정할 만한 사항 없음
- 문제 display 포맷 변경 시 수정은 quiz.py 파일에서 Quiz 클래스 중 display() 메쏘드
- 그 외 모든 수정은 quiz_game.py 파일의 QuizGame 클래스를 수정해야 함
  메뉴 구조 변경은 run() 메쏘드 수정하고 해당 메쏘드를 신규/추가, 정답 채첨이나 점수 계산은 play_quiz() 메쏘스 수정

### main.py

```python
from quiz_game import QuizGame

def main():
   game = QuizGame()
   game.run()

if __name__ == "__main__":
   main()
```


### quiz.py

```python
class Quiz:

   def __init__(self, question, choices, answer):
       self.question = question          # 문제 (str)
       self.choices = choices            # 선택지 (list, 길이 4)
       self.answer = answer              # 정답 (int, 1~4)

   def display(self):                    # 퀴즈문제 출력
       print(self.question)
       print()

       for i, choice in enumerate(self.choices, start=1):
           print(f"{i}. {choice}")

   def check_answer(self, user_answer):  # 정답 체크
       return user_answer == self.answer
```


### quiz_game.py

```python
import json
import os
from quiz import Quiz

class QuizGame:

   def __init__(self):
       self.quizzes = []
       self.best_score = 0

       self.load_data()
       if not self.quizzes:          # 데이터가 없을 경우
           self.load_default_quizzes()


   def run(self):                       # 메뉴 표시 및 사용자 입력에 따른 세부 메쏘드 호출
       try:

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
                   print("퀴즈 종료")
                   self.save_data()
                   break

       except (KeyboardInterrupt, EOFError):

           print("\n프로그램 중단, 데이터 저장 후 종료")
           self.save_data()

       except Exception as e:

           print(f"\n예기치 못한 오류 발생: {e}")
           print("데이터 저장 후 종료")
           self.save_data()


   def show_menu(self):                         # 메뉴 표시
       print("=" * 40)
       print("나만의 퀴즈 게임")
       print("=" * 40)
       print("1. 퀴즈 풀기")
       print("2. 퀴즈 추가")
       print("3. 퀴즈 목록")
       print("4. 점수 확인")
       print("5. 종료")
       print("=" * 40)


   def get_user_input(self):                    # 사용자 입력 처리

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

   def play_quiz(self):                         # 퀴즈 풀기

       if not self.quizzes:
           print("등록된 퀴즈가 없습니다.")
           return

       print("-" * 40)
       print("\n퀴즈를 시작합니다!")
       print(f"(총 {len(self.quizzes)}문제)")
       print("-" * 40)

       score = 0

       for idx, quizob in enumerate(self.quizzes, start=1):     # 퀴즈 문제 표시
           print(f"\n[문제 {idx}]")
           quizob.display()

           user_answer = self.get_answer_input()                # 퀴즈 답 입력

           if quizob.check_answer(user_answer):                 # 퀴즈 정답 체크
               print("정답입니다!")
               score += 1
           else:
               print(f"오답! 정답은 {quizob.answer}번")

       print("\n" + "=" * 40)
       print(f"결과: {len(self.quizzes)}문제 중 {score}문제 정답!( {score/len(self.quizzes)*100:.0f}점)")

       if score > self.best_score:             # 최고 점수 갱신
           print("새로운 최고 점수입니다!")
           self.best_score = score


   def get_answer_input(self):                              # 퀴즈 선택지 중 풀려는 답 입력 받아서 처리

       while True:

           try:
               user_input = input("\n정답 입력(1~4): ").strip()

               if not user_input:
                   print("빈 입력, 다시 정답 입력")
                   continue

               answer = int(user_input)

               if answer < 1 or answer > 4:
                   print("1~4 숫자 입력")
                   continue

               return answer

           except ValueError:
               print("숫자 입력")

           except (KeyboardInterrupt, EOFError):
               print("\n프로그램 종료")
               self.save_data()
               exit()


   def add_quiz(self):                                    # 신규 퀴즈 추가
       print("\n새로운 퀴즈를 추가합니다.")

       try:
           question = input("문제를 입력하세요: ").strip()   # 문제 입력

           if not question:
               print("문제는 비어 있을 수 없습니다.")
               return

           choices = []                                    # 선택지 입력

           for i in range(1, 5):
               choice = input(f"선택지 {i}: ").strip()

               if not choice:
                   print("선택지 비어 있음, 다시 입력")
                   return

               choices.append(choice)

           answer = self.get_answer_input()                # 정답 입력
           new_quiz = Quiz(question, choices, answer)      # Quiz 객체 생성

           self.quizzes.append(new_quiz)                   # 리스트에 추가
           print("퀴즈가 추가되었습니다!")

       except (KeyboardInterrupt, EOFError):
           print("\n입력 중단. 프로그램 종료")
           self.save_data()
           exit()


   def list_quizzes(self):                          # 저장돼 있는 퀴즈 문제만 보여줌(선택지는 미 표시)

       if not self.quizzes:
           print("\n등록된 퀴즈 없음\n")
           return

       print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
       print("-" * 40)

       for idx, quizob in enumerate(self.quizzes, start=1):
           print(f"[{idx}] {quizob.question}")

       print("-" * 40)
       print()

   def show_score(self):                        # 최고 점수, 전체 문제 수와 정답 수 표시

       print("\n점수 확인")

       if self.best_score == 0:
           print("0점(아직 퀴즈 풀기 전)\n")
           return

       total = len(self.quizzes)

       print("-" * 40)
       print(f"최고 점수: {self.best_score/total*100:.0f}점 ({total}문제 중 {self.best_score}문제 정답)")
       print("-" * 40)


   def load_data(self):                                         # 저장된 파일에서 퀴즈 문제 읽어서 내부 data로 저장

       if not os.path.exists("state.json"):
           print("기본 퀴즈 사용")
           return

       try:
           with open("state.json", "r", encoding="utf-8") as fileob:
               data = json.load(fileob)

           self.quizzes = [
               Quiz(quizfileold["question"], quizfileold["choices"], quizfileold["answer"])
               for quizfileold in data.get("quizzes", [])
           ]

           self.best_score = data.get("best_score", 0)
           print(f"저장된 데이터 로드. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")

       except (json.JSONDecodeError, KeyError, TypeError):
           print("데이터 파일 손상, 기본 데이터로 복구")

           self.load_default_quizzes()
           self.best_score = 0

       except Exception as e:
           print(f"데이터 로드 중 오류 발생: {e}")


   def save_data(self):                                 # 새로운 퀴즈 문제 추가하여 파일로 저장

       data = {
           "quizzes": [
               {
                   "question": quizob.question,
                   "choices": quizob.choices,
                   "answer": quizob.answer
               }
               for quizob in self.quizzes
           ],
           "best_score": self.best_score
       }

       try:
           with open("state.json", "w", encoding="utf-8") as fileob:
               json.dump(data, fileob, ensure_ascii=False, indent=4)

       except Exception as e:
           print(f"데이터 저장 중 오류 발생: {e}")


   def load_default_quizzes(self):          # 퀴즈 문제가 없을 경우에 최초 문제 5개 제시

       self.quizzes = [

           Quiz(
               "Python의 창시자는?",
               ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"],
               2
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
```
