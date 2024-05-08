import pytest
from src.main import sum, is_greater_than, login

def test_sum():
    assert sum(2, 5) == 7

def test_is_greater_than():
    assert is_greater_than(10, 2)

@pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (5, 1, 6),
            (7, sum(1, 1), 9),
            (sum(14, 1), 5, 20),
            (-7, 10, sum(-7, 10)),
        ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected

def test_login_pass():
    login_passes = login("jgarcia", "123456")# este valor da true
    assert login_passes 

def test_login_fail():
    login_passes = login("jgarcia_xd", "12345695")# este vaolr da false
    assert not login_passes


