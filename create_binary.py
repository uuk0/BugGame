import sys
import os
import subprocess


local = os.path.dirname(__file__)
subprocess.call(
    [
        sys.executable,
        "-m",
        "PyInstaller",
        "-F",
        "--name",
        "BugGame",
        local+"/__main__.py"
    ]
)

