class Example:
    def __init__(self, message):
        self.message = message

    def get_example_message(self):
        return self.message

    def get_ascii_art(self):
        try:
            from pyfiglet import Figlet
            figlet = Figlet()
            return figlet.renderText(self.message)
        except ImportError:
            return "pyfiglet is not installed."
