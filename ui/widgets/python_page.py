import customtkinter as ctk

from services.python_teacher_service import PythonTeacherService


class PythonPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.teacher = PythonTeacherService()

        ctk.CTkLabel(
            self,
            text="💻 AI Python Teacher",
            font=("Arial", 28, "bold")
        ).pack(pady=15)

        self.topic = ctk.CTkEntry(
            self,
            placeholder_text="Example: Variables, Loops, Functions..."
        )

        self.topic.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Teach Me",
            command=self.teach
        ).pack(pady=10)

        self.output = ctk.CTkTextbox(
            self,
            height=500
        )

        self.output.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def teach(self):

        topic = self.topic.get().strip()

        if not topic:
            return

        self.output.delete("1.0", "end")
        self.output.insert("end", "Preparing lesson...\n\n")
        self.update()

        try:

            lesson = self.teacher.teach(topic)

            self.output.delete("1.0", "end")
            self.output.insert("end", lesson)

        except Exception as e:

            self.output.delete("1.0", "end")
            self.output.insert("end", f"Error:\n{e}")