import customtkinter as ctk

from services.quiz_service import QuizService


class QuizPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = QuizService()

        ctk.CTkLabel(
            self,
            text="❓ AI Quiz Generator",
            font=("Arial", 28, "bold")
        ).pack(pady=15)

        self.topic = ctk.CTkEntry(
            self,
            placeholder_text="Enter Topic..."
        )

        self.topic.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.difficulty = ctk.CTkOptionMenu(
            self,
            values=[
                "Easy",
                "Medium",
                "Hard"
            ]
        )

        self.difficulty.pack(pady=10)

        self.questions = ctk.CTkOptionMenu(
            self,
            values=[
                "5",
                "10",
                "15",
                "20"
            ]
        )

        self.questions.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Generate Quiz",
            command=self.generate
        ).pack(pady=10)

        self.output = ctk.CTkTextbox(
            self,
            height=450
        )

        self.output.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def generate(self):

        topic = self.topic.get().strip()

        if topic == "":
            return

        self.output.delete("1.0", "end")

        self.output.insert(
            "end",
            "Generating Quiz...\n\n"
        )

        self.update()

        try:

            quiz = self.service.generate(
                topic,
                self.difficulty.get(),
                self.questions.get()
            )

            self.output.delete("1.0", "end")

            self.output.insert(
                "end",
                quiz
            )

        except Exception as e:

            self.output.delete("1.0", "end")

            self.output.insert(
                "end",
                str(e)
            )