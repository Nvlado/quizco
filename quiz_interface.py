from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizco")
        self.window.config(padx=100, pady=100, bg="blue")
        self.score_label = Label(text=f"Score: 0", font=("Arial", 20), fg="white", bg="blue")
        self.score_label.grid(column=0, row=0)
        self.canvas = Canvas(width=500, height=400, bg="white")
        self.question_text = self.canvas.create_text(250, 200, width=400, font=("Arial", 20))
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        self.yes_button = Button(text="Y", font=("Arial", 20), highlightthickness=0, command=self.true_pressed)
        self.yes_button.grid(column=0, row=2)
        self.no_button = Button(text="N", font=("Arial", 20), highlightthickness=0, command=self.false_pressed)
        self.no_button.grid(column=1, row=2)
        self.get_new_question()
        self.window.mainloop()


    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the of the Quizco")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.get_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_new_question)