from ..targets.base import BaseTarget
from .base import BaseFormatter


class PlainNewlineFormatter(BaseFormatter):
    def format(self, target: BaseTarget) -> str:
        if target.path.resolve().is_relative_to(self.cwd):
            return f"{target.path.name}\n"
        else:
            return f"{target.path}\n"
