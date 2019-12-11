# Write a program that prints one line for each number from 1 to 100
# For multiples of three print Fizz instead of the number
# For the multiples of five print Buzz instead of the number
# For numbers which are multiples of both three and five print FizzBuzz instead of the number
from fizzbuzz import fizzbuzz
import pytest

divisible_by_tree = [3, 6, 9, 12]

divisible_by_five = [5, 10, 20, 500]

divisible_by_both = [15, 30, 45, 60]

divisible_by_none = [0, 1, 2, 4, 7, 8, 11]


# http://doc.pytest.org/en/latest/example/parametrize.html
# generators could also be used instead
@pytest.mark.parametrize("number", divisible_by_tree)
def test_fizz(number):
    assert fizzbuzz(number) == 'Fizz'


@pytest.mark.parametrize("number", divisible_by_five)
def test_buzz(number):
    assert fizzbuzz(number) == 'Buzz'


def test_fizzbuzz():
    assert fizzbuzz(15) == 'FizzBuzz'


@pytest.mark.parametrize("number", divisible_by_none)
def test_fizzbuzz_for_number(number):
    assert fizzbuzz(2) == 2
