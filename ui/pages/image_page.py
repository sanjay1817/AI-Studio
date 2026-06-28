import customtkinter as ctk
from PIL import ImageTk

from services.image_service import ImageService


class ImagePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = ImageService()

        title = ctk.CTkLabel(
            self,
            text="🎨 AI Image Generator",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=20)

        self.prompt = ctk.CTkEntry(
            self,
            width=700,
            placeholder_text="Example : Flying elephant in space"
        )

        self.prompt.pack(pady=10)

        self.button = ctk.CTkButton(
            self,
            text="Generate Image",
            command=self.generate
        )

        self.button.pack(pady=10)

        self.status = ctk.CTkLabel(
            self,
            text=""
        )

        self.status.pack()

        self.image_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.image_label.pack(pady=20)

    def generate(self):

        prompt = self.prompt.get()

        if prompt == "":
            return

        self.status.configure(text="Generating Image...")

        self.update()

        try:

            image = self.service.generate(prompt)

            image.thumbnail((700, 500))

            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)

            self.image_label.image = photo

            self.status.configure(text="✅ Image Generated")

        except Exception as e:

            self.status.configure(text=str(e))