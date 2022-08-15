from pathlib import Path


class BaseFormatter:
    def __init__(self):
        self.cwd = Path.cwd()
