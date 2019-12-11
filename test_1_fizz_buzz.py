# Write a program that prints one line for each number from 1 to 100
# For multiples of three print Fizz instead of the number
# For the multiples of five print Buzz instead of the number
# For numbers which are multiples of both three and five print FizzBuzz instead of the number
from fizzbuzz import fizzbuzz
import pytest


divisible_by_tree = [3, 6, 9, 12, 15, 300]


@pytest.mark.parametrize("num", divisible_by_tree)
def test_fizz(num):
    assert fizzbuzz(num) == 'Fizz'


def test_buzz():
    assert fizzbuzz(5) == 'Buzz'
