"""Application entry point for the Typing Test.

Run with: ``python main.py``
"""
import os
import sys

# Make the modules inside ``src`` importable when running from the project root.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from PyQt5.QtWidgets import QApplication  # noqa: E402

from head_menu import Head_Menu  # noqa: E402


def except_hook(cls, exception, traceback):
    """Keep tracebacks visible instead of the app silently dying."""
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QApplication(sys.argv)
    window = Head_Menu()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
