import sys
import os
import subprocess


local = os.path.dirname(__file__)
subprocess.call(
    [
        sys.executable,
        "-OO",
        "-m",
        "PyInstaller",
        "-F",
        "--name",
        "BugGame",
        "--windowed",
        local+"/__main__.py"
    ]
)


if sys.argv[1] == "--run":
    subprocess.call(["./dist/BugGame.exe"] + sys.argv[2:])

