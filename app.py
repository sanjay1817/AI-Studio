from core.theme import Theme
from ui.dashboard import Dashboard


class App:

    def __init__(self):

        Theme.initialize()

        self.window = None

    def start(self):

        self.window = Dashboard()

        self.window.mainloop()