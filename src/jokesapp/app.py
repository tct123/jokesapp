"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr


class JokesApp(toga.App):
    def startup(self):

        csv_file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        joke = toga.Label(tr(csv_file=csv_file, target_key="JOKE1"))
        main_box.add(joke)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return JokesApp()
