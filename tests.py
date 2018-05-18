import subprocess
import os


def test_avalon_help():
    returncode = subprocess.call(["avalon", "--help"], shell=True)

    msg = "'avalon --help' did not execute correctly."
    assert returncode == 0, msg


def test_submodules_exists():
    git_directory = os.path.abspath(
        os.path.join(__file__, "..", "bin", "avalon-setup", "git")
    )
    assert os.path.exists(git_directory)
