from pathlib import Path
from unittest import TestCase

from lib.formatters.plain_newline import PlainNewlineFormatter
from lib.targets.file import FileTarget


class PlainNewlineFormatterTestCase(TestCase):
    def test_formats_files_in_current_path(self):
        target = FileTarget(Path("test.txt"))
        formatter = PlainNewlineFormatter()
        self.assertEqual(formatter.format(target), "test.txt\n")

    def test_formats_files_outside_current_path(self):
        target = FileTarget(Path("../../test.txt"))
        formatter = PlainNewlineFormatter()
        self.assertEqual(formatter.format(target), "../../test.txt\n")
