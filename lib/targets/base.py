from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class TargetTypes(Enum):
    DIRECTORY = 1
    FILE = 2


@dataclass
class BaseTarget:
    path: Path
    type: TargetTypes

    def __init__(self, path: Path):
        if not hasattr(self, "type"):
            raise NotImplementedError(
                "You need to set the type for BaseTarget subclass"
            )

        self.path = path
