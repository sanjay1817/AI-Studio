import customtkinter as ctk

from ui.widgets.card import FeatureCard


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master, page_callback):
        super().__init__(master)

        self.page_callback = page_callback

        title = ctk.CTkLabel(
            self,
            text="Welcome 👋",
            font=("Arial",30,"bold")
        )

        title.pack(pady=(20,5))

        subtitle = ctk.CTkLabel(
            self,
            text="Choose an AI Tool",
            font=("Arial",15)
        )

        subtitle.pack(pady=(0,20))

        grid = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        grid.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=20
        )

        for i in range(3):
            grid.grid_columnconfigure(i, weight=1)

        features = [

            ("🤖","AI Chat","Talk with Gemini AI"),

            ("🎨","Image Generator","Generate AI Images"),

            ("📖","Story Generator","Create Stories"),

            ("❓","Quiz Generator","Generate Quiz"),

            ("💻","Python Teacher","Learn Python"),

            ("⚙","Settings","Application Settings")

        ]

        row = 0
        col = 0

        for icon,title,desc in features:

            card = FeatureCard(

                grid,

                icon,

                title,

                desc,

                command=lambda t=title:self.page_callback(t)

            )

            card.grid(

                row=row,

                column=col,

                padx=15,

                pady=15,

                sticky="nsew"

            )

            col += 1

            if col == 3:

                col = 0

                row += 1