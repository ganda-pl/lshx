from pathlib import Path
from unittest import TestCase

from lib.formatters.plain import PlainFormatter
from lib.targets.file import FileTarget


class PlainFormatterTestCase(TestCase):
    def test_formats_files_in_current_path(self):
        target = FileTarget(Path("test.txt"))
        formatter = PlainFormatter()
        self.assertEqual(formatter.format(target), "test.txt ")

    def test_formats_files_outside_current_path(self):
        target = FileTarget(Path("../../test.txt"))
        formatter = PlainFormatter()
        self.assertEqual(formatter.format(target), "../../test.txt ")
