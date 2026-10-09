from highfive import is_highfive
import pytest
# 1. confirm that 105 is a high five
# 2. confirm that 100 is not a high five
# 3. confirm that 106 is not a high five

# your code here


def test_highfive():
    assert is_highfive(105)
    assert not is_highfive(100)
    assert not is_highfive(106)


@pytest.mark.parametrize("number, expected", [(105, True), (100, False), (106, False)])
def test_all(number, expected):
    assert is_highfive(number) == expected
