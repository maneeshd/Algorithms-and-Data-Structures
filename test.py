from pylint import epylint as lint
from os import path
from re import compile


CUR_DIR = path.realpath(path.dirname(__file__))
SCORE_REGEX = compile(r"Your code has been rated at ([\d.]+)/10")

PYLINT_OPTIONS = f"{CUR_DIR} --max-line-length=120 --score=y --output-format=parseable"


def test_pylint():
    stdout, stderr = lint.py_run(PYLINT_OPTIONS, return_std=True)
    match = SCORE_REGEX.search(stdout.read())
    if match:
        score = float(match.group(1))
        print(f"Score={score}")
        assert score > 8.5
    else:
        print(stdout.read())
        print(stderr.read())
        raise AssertionError("Failed to get pylint test score")
