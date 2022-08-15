from .base import BaseFormatter
from ..targets.base import BaseTarget


class PlainFormatter(BaseFormatter):
    def format(self, target: BaseTarget) -> str:
        if target.path.resolve().is_relative_to(self.cwd):
            return f"{target.path.name} "
        else:
            return f"{target.path} "
