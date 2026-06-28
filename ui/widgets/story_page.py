import customtkinter as ctk

from services.story_service import StoryService


class StoryPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = StoryService()

        ctk.CTkLabel(
            self,
            text="📖 AI Story Generator",
            font=("Arial", 28, "bold")
        ).pack(pady=15)

        self.topic = ctk.CTkEntry(
            self,
            placeholder_text="Story Topic..."
        )

        self.topic.pack(fill="x", padx=20, pady=10)

        self.genre = ctk.CTkOptionMenu(
            self,
            values=[
                "Adventure",
                "Fantasy",
                "Science Fiction",
                "Comedy",
                "Mystery",
                "Motivational"
            ]
        )

        self.genre.pack(pady=10)

        self.length = ctk.CTkOptionMenu(
            self,
            values=[
                "Short",
                "Medium",
                "Long"
            ]
        )

        self.length.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Generate Story",
            command=self.generate
        ).pack(pady=10)

        self.story = ctk.CTkTextbox(
            self,
            height=450
        )

        self.story.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def generate(self):

        topic = self.topic.get().strip()

        if topic == "":
            return

        self.story.delete("1.0", "end")

        self.story.insert(
            "end",
            "Generating story...\n\n"
        )

        self.update()

        try:

            result = self.service.generate(
                topic,
                self.genre.get(),
                self.length.get()
            )

            self.story.delete("1.0", "end")

            self.story.insert(
                "end",
                result
            )

        except Exception as e:

            self.story.delete("1.0", "end")

            self.story.insert(
                "end",
                str(e)
            )