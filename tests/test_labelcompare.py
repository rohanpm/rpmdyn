import pytest


@pytest.mark.parametrize(
    "evr1,evr2,result",
    [
        [("0", "0", "0"), ("1", "1", "1"), -1],
        [("2", "0", "0"), ("1", "1", "1"), 1],
        [("", "0", "0"), ("", "1", "1"), -1],
    ],
)
def test_labelCompare(rpm, evr1, evr2, result):
    assert rpm.labelCompare(evr1, evr2) == result
