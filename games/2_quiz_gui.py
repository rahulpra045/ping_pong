from tkinter import*
from tkinter import simpledialog,messagebox

main = Tk()
main.withdraw()
main.geometry("800x500")


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
    user_answer = simpledialog.askstring(questions[i], "Answer: ")

    if user_answer == answer[i]:
        messagebox.showinfo("Correct", "Correct")
        score = score +1
    else:
        messagebox.showinfo("Wrong", "Wrong")
messagebox.showinfo("Score", str(score))
