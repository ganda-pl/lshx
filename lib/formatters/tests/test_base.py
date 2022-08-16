from pathlib import Path
from unittest import TestCase

from lib.formatters.base import BaseFormatter
from lib.targets.file import FileTarget


class BaseFormatterTestCase(TestCase):
    def test_raises_not_implemented_when_subclass_doesnt_implement_format(self):
        class NoFormatMethodFormatter(BaseFormatter):
            pass

        with self.assertRaises(NotImplementedError):
            target = FileTarget(Path("test.txt"))
            formatter = NoFormatMethodFormatter()
            formatter.format(target)
