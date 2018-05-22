import subprocess
import os


def test_avalon_help():
    returncode = subprocess.call(["avalon", "--help"], shell=True)

    msg = "'avalon --help' did not execute correctly."
    assert returncode == 0, msg


def test_submodules_exists():
    git_directory = os.path.abspath(
        os.path.join(__file__, "..", "..", "bin", "avalon-setup", "git")
    )
    assert os.path.exists(git_directory)


def test_default_database_creation():
    subprocess.call(["server"], shell=True)

    msg = "Failed to create default database."
    assert os.path.exists("c:\\data\\db"), msg


def test_custom_database_location():
    subprocess.call(["server", "c:\\data\\custom"], shell=True)

    msg = "Failed to create default database."
    assert os.path.exists("c:\\data\\custom"), msg
