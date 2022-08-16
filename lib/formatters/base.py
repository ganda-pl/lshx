from abc import abstractmethod
from pathlib import Path

from lib.targets.base import BaseTarget


class BaseFormatter:
    def __init__(self):
        self.cwd = Path.cwd()

    @abstractmethod
    def format(self, target: BaseTarget) -> str:
        raise NotImplementedError("Format method has to be implemented in subclass")
