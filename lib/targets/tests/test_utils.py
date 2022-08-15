from pathlib import Path
from unittest import TestCase

from lib.targets.directory import DirectoryTarget
from lib.targets.file import FileTarget
from lib.targets.utils import split_targets


class SplitTargetsTestCase(TestCase):
    def test_split_targets_files_only(self):
        targets = [
            FileTarget(path=Path("test1.txt")),
            FileTarget(path=Path("test2.txt")),
        ]

        non_containers, containers = split_targets(targets)

        self.assertEqual(len(non_containers), 2)
        self.assertEqual(len(containers), 0)

    def test_split_targets_directories_only(self):
        targets = [
            DirectoryTarget(path=Path("test1")),
            DirectoryTarget(path=Path("test2")),
        ]

        non_containers, containers = split_targets(targets)

        self.assertEqual(len(non_containers), 0)
        self.assertEqual(len(containers), 2)

    def test_split_targets_mix(self):
        targets = [
            FileTarget(path=Path("test1.txt")),
            DirectoryTarget(path=Path("test2")),
        ]

        non_containers, containers = split_targets(targets)

        self.assertEqual(len(non_containers), 1)
        self.assertEqual(len(containers), 1)
