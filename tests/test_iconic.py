import pytest

import iconic


def test_success():
    svg = iconic.load_icon("announcement")
    assert svg.startswith("<svg")


def test_fail_unknown():
    with pytest.raises(iconic.IconDoesNotExist) as excinfo:
        iconic.load_icon("nooooo")

    assert excinfo.value.args == ("The icon 'nooooo' does not exist.",)
