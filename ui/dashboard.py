"""
ui/dashboard.py
"""

import customtkinter as ctk
import config

from ui.widgets.sidebar import Sidebar
from ui.widgets.header import Header

from ui.pages.dashboard_page import DashboardPage
from ui.pages.chat_page import ChatPage
from ui.pages.image_page import ImagePage
from ui.pages.story_page import StoryPage
from ui.pages.quiz_page import QuizPage
from ui.pages.python_page import PythonPage
from ui.pages.settings_page import SettingsPage


class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(config.APP_NAME)
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.minsize(config.MIN_WIDTH, config.MIN_HEIGHT)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Main Container
        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.grid(row=0, column=1, sticky="nsew")

        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Header
        self.header = Header(self.container)
        self.header.grid(row=0, column=0, sticky="ew", padx=20, pady=(20,10))

        # First Page
        self.current_page = None
        self.show_page("Dashboard")

        # Sidebar callback
        self.sidebar.menu_callback = self.show_page

    # ----------------------------------------------------

    def show_page(self, page_name):

        if self.current_page:
            self.current_page.destroy()

        pages = {
            "Dashboard": lambda: DashboardPage(self.container, self.show_page),
            "AI Chat": lambda: ChatPage(self.container),
            "Image Generator": lambda: ImagePage(self.container),
            "Story Generator": lambda: StoryPage(self.container),
            "Quiz Generator": lambda: QuizPage(self.container),
            "Python Teacher": lambda: PythonPage(self.container),
        }

        self.current_page = pages.get(
            page_name,
            pages["Dashboard"]
        )()

        self.current_page.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(10,20)
        )
