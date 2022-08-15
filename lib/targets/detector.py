import sys
from pathlib import Path
from typing import Type

from .base import BaseTarget
from .directory import DirectoryTarget
from .exceptions import TargetNotFoundError
from .file import FileTarget


class TargetDetector:
    @staticmethod
    def target_exists(path: Path) -> bool:
        """
        Checks if path exist in the filesystem
        """
        return path.exists()

    @staticmethod
    def get_target_class(path: Path) -> Type[BaseTarget]:
        """
        Checks the type of provided path (file, dir, symlink, etc. ) and returns a corresponding BaseTarget subclass
        """
        if path.is_dir():
            return DirectoryTarget
        elif path.is_file():
            return FileTarget
        else:
            raise ValueError("Unsupported target type")

    @staticmethod
    def get_target(pathstr: str) -> BaseTarget:
        """
        Returns a target object for given path. Raises TargetNotFoundError, when given path does not exist
        """
        path = Path(pathstr)
        if not TargetDetector.target_exists(path):
            raise TargetNotFoundError(f"lshx: {path.name}: No such file or directory")
        target_class = TargetDetector.get_target_class(path)
        return target_class(path)

    @staticmethod
    def detect(paths: list[str]) -> list[BaseTarget]:
        """
        Processes the list of paths and returns a list of filesystem targets
        """

        targets: list[BaseTarget] = []

        # if list of paths is empty, return current directory as target
        if not paths:
            targets = [DirectoryTarget(Path.cwd())]

        # proceed with target detection
        else:
            for path in paths:
                try:
                    targets.append(TargetDetector.get_target(path))
                except TargetNotFoundError as exc:
                    print(exc, file=sys.stderr)

        return targets
