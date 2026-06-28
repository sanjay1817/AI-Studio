class Router:

    def __init__(self):
        self.current_page = None

    def navigate(self, page):
        self.current_page = page
