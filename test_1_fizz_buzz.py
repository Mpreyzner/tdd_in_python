# Write a program that prints one line for each number from 1 to 100
# For multiples of three print Fizz instead of the number
# For the multiples of five print Buzz instead of the number
# For numbers which are multiples of both three and five print FizzBuzz instead of the number
from fizzbuzz import fizzbuzz
import pytest

divisible_by_tree = [3, 6, 9, 12, 15, 300]

divisible_by_five = [5, 10, 15, 20, 500]


# http://doc.pytest.org/en/latest/example/parametrize.html
@pytest.mark.parametrize("number", divisible_by_tree)
def test_fizz(number):
    assert fizzbuzz(number) == 'Fizz'


@pytest.mark.parametrize("number", divisible_by_five)
def test_buzz(number):
    assert fizzbuzz(number) == 'Buzz'
