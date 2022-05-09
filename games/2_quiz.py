
questions = [ "what is your name?",
              "what is you age?",
              "Are you a Student?",
              "What is your Gender?" ]

answer = ["Rahul",
          "19",
          "Yes",
          "Male"]

score =0

for i in range(0,len(questions)):
    print(questions[i])
    user_answer = input("Answer: ")

    if user_answer == answer[i]:
        print("Correct")
        score = score +1
    else:
        print("Incorrect")    

print(f"score {score}")
