from driftdetect.cli import valid_directory
from driftdetect.config import Config


def test_valid_directory():
    config = Config("tests", "localhost")
    assert valid_directory(config)
    config.drift_detector_directory = "temp"
    assert not valid_directory(config)
