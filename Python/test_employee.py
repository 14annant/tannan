'''Test program with fixtures. Removes the effort of creating an employee in each method'''

import pytest
from employee import Employee   


@pytest.fixture
def employee_tom():
    tom = Employee('tom','annan',100000)
    return tom


def test_give_default_raise(employee_tom: Employee):
 #   tom = Employee('tom','annan',100000)
 #   result = tom.give_raise()
    assert employee_tom.give_raise() == 105000 

def test_give_custom_raise(employee_tom: Employee):
 #   tom = Employee('tom','annan',100000)
    raise_amount = 200000
 #   result = raise_amount + employee_tom.annual_salary
    assert employee_tom.give_raise(raise_amount) == 300000