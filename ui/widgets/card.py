import customtkinter as ctk


class FeatureCard(ctk.CTkFrame):

    def __init__(self, master, icon, title, description, command=None):
        super().__init__(master, corner_radius=15)

        self.command = command

        self.configure(height=180)

        self.bind("<Button-1>", self.on_click)

        self.icon = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 42)
        )
        self.icon.pack(pady=(20, 10))
        self.icon.bind("<Button-1>", self.on_click)

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Arial", 18, "bold")
        )
        self.title.pack()
        self.title.bind("<Button-1>", self.on_click)

        self.description = ctk.CTkLabel(
            self,
            text=description,
            font=("Arial", 12),
            wraplength=180
        )
        self.description.pack(pady=(5, 20))
        self.description.bind("<Button-1>", self.on_click)

    def on_click(self, event=None):
        if self.command:
            self.command()
