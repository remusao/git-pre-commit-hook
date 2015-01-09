"""Check files with pylint."""

from __future__ import print_function
import StringIO
from pylint import lint
from pylint.reporters.text import TextReporter


def check(file_staged_for_commit, options):
    arguments = [
        "--errors-only",
        "-r", "n",
        "-f", "colorized"]
    pylint_output = StringIO.StringIO()
    lint.Run(
        [file_staged_for_commit.path] + arguments,
        reporter=TextReporter(pylint_output),
        exit=False)
    pylint_output = pylint_output.getvalue().strip()
    print(pylint_output)
    return pylint_output == ''
