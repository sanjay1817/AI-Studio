import customtkinter as ctk
from services.gemini_service import GeminiService


class ChatPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.ai = GeminiService()

        ctk.CTkLabel(
            self,
            text="🤖 AI Chat",
            font=("Arial", 28, "bold")
        ).pack(pady=10)

        self.chat = ctk.CTkTextbox(
            self,
            width=900,
            height=450
        )
        self.chat.pack(fill="both", expand=True, padx=20, pady=10)

        bottom = ctk.CTkFrame(self)
        bottom.pack(fill="x", padx=20, pady=10)

        self.entry = ctk.CTkEntry(
            bottom,
            placeholder_text="Ask anything...",
            height=40
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0,10)
        )

        send = ctk.CTkButton(
            bottom,
            text="Send",
            command=self.send_message
        )

        send.pack(side="right")

    def send_message(self):

        question = self.entry.get().strip()

        if question == "":
            return

        self.chat.insert("end", f"\n🧑 You:\n{question}\n\n")

        self.entry.delete(0, "end")

        self.update()

        try:

            answer = self.ai.ask(question)

            self.chat.insert(
                "end",
                f"🤖 Gemini:\n{answer}\n\n"
            )

        except Exception as e:

            self.chat.insert(
                "end",
                f"❌ Error:\n{e}\n\n"
            )

        self.chat.see("end")
