import os
import subprocess
import sys

import main

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_locate_existing_file():
    os.chdir(HERE)
    assert main.locate_project_file("main.py") == "main.py"


def test_locate_missing_file():
    os.chdir(HERE)
    assert main.locate_project_file("does-not-exist.xyz") is None


def test_prediction_runs_end_to_end():
    """Runs the Weka model through JPype on instance 8, as the CI did before."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        input="8\n",
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0, result.stderr
    assert "Final Filtered Decision" in result.stdout
