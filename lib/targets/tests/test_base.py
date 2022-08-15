from unittest import TestCase

from lib.targets.base import BaseTarget


class BaseTargetTests(TestCase):
    def test_base_target_subclasses_raise_not_implemented_on_unset_type(self):
        class TestTargetNoType(BaseTarget):
            pass

        with self.assertRaises(NotImplementedError):
            TestTargetNoType(".")

    def test_base_target_subclasses_can_be_instantiated_with_a_defined_type(self):
        class TestTargetNoType(BaseTarget):
            type = "test"

        TestTargetNoType(".")
