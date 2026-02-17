from tkinter import *
from QUIZ_BRAIN import QuizBrain

THEME_COLOR = "#375362"
Wrong_img_path = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng\FALSE.png"
True_img_path = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng\TRUE.png"

class QuizUi:
    def __init__(self, Quiz: QuizBrain):
        self.quiz = Quiz

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # ⭐ QUESTION NUMBER LABEL (UPGRADE)
        self.Question_no_label = Label(text="Question: 0",bg=THEME_COLOR,
                                       fg="white",font=("Arial", 15, "italic"))
        self.Question_no_label.grid(column=0, row=0)

        self.Score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="#FFFFFF",
                                 font=("Arial", 15, "italic"))
        self.Score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=290, highlightthickness=0, bg="white")
        self.Question_txt = self.canvas.create_text(
            160, 120,
            width=280,
            text="There a Questions",
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.wrong = PhotoImage(file=Wrong_img_path)
        self.Wrong_Button = Button(
            image=self.wrong,
            highlightthickness=0,
            command=self.False_Pressed
        )
        self.Wrong_Button.grid(row=4, column=0, pady=20)

        self.Right = PhotoImage(file=True_img_path)
        self.Right_Button = Button(
            image=self.Right,
            highlightthickness=0,
            command=self.True_Pressed
        )
        self.Right_Button.grid(row=4, column=1, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():

            self.Score_label.config(text=f"Score: {self.quiz.score}")

            # ⭐ UPDATE QUESTION NUMBER (UPGRADE)
            self.Question_no_label.config(
                text=f"Question: {self.quiz.question_number + 1}"
            )

            Quiz_Question = self.quiz.next_question()
            self.canvas.itemconfig(self.Question_txt, text=Quiz_Question)

        else:
            self.canvas.itemconfig(
                self.Question_txt,
                text="You Have Reached the End of the Game"
            )
            self.Wrong_Button.config(cursor="hand2")
            self.Right_Button.config(cursor="hand2")

    def True_Pressed(self):
        is_right = self.quiz.check_answer("True")
        self.Give_Feedback(is_right)

    def False_Pressed(self):
        is_right = self.quiz.check_answer("False")
        self.Give_Feedback(is_right)

    def Give_Feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)