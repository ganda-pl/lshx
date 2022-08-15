from unittest import TestCase
from unittest.mock import patch

from lib.targets.base import TargetTypes
from lib.targets.detector import TargetDetector


class TargetDetectorTests(TestCase):
    def test_detector_returns_current_directory_target_when_no_paths_are_provided(self):
        targets = TargetDetector().detect(paths=[])
        self.assertEqual(len(targets), 1)
        self.assertEqual(targets[0].type, TargetTypes.DIRECTORY)

    def test_detector_omits_non_existent_files(self):
        targets = TargetDetector().detect(paths=["this_file_does_not_exist.txt"])
        self.assertEqual(len(targets), 0)

    @patch("lib.targets.detector.Path", autospec=True)
    def test_detector_on_directories(self, path_mock):
        path_mock.return_value.exists.return_value = True
        path_mock.return_value.is_dir.return_value = True
        path_mock.return_value.is_file.return_value = False
        targets = TargetDetector().detect(paths=["aDirectory"])
        self.assertEqual(len(targets), 1)
        self.assertEqual(targets[0].type, TargetTypes.DIRECTORY)

    @patch("lib.targets.detector.Path", autospec=True)
    def test_detector_on_files(self, path_mock):
        path_mock.return_value.exists.return_value = True
        path_mock.return_value.is_dir.return_value = False
        path_mock.return_value.is_file.return_value = True
        targets = TargetDetector().detect(paths=["aFile.txt"])
        self.assertEqual(len(targets), 1)
        self.assertEqual(targets[0].type, TargetTypes.FILE)

    @patch("lib.targets.detector.Path", autospec=True)
    def test_detector_on_unsupported_type(self, path_mock):
        path_mock.return_value.exists.return_value = True
        path_mock.return_value.is_dir.return_value = False
        path_mock.return_value.is_file.return_value = False
        with self.assertRaises(ValueError):
            TargetDetector().detect(paths=["/var/run/socket"])
