from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here",
            fill=THEME_COLOR,
            font=("Arial", 15, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 12, 'bold'), fg="white")
        self.score_label.grid(row=0, column=1)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=false_image, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=true_image, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.windows.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.windows.after(1000, self.get_next_question)