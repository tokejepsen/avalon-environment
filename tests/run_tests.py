import os
import sys
import subprocess


subprocess.call(["pip", "install", "pytest"])

import pytest

sys.exit(
    pytest.main(
        [os.path.abspath(os.path.join(__file__, "..", "tests.py"))]
    )
)
