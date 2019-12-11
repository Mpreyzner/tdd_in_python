# https://github.com/TDD-Katas/frequent-words

# Given a list of words, print the list of top N most frequently occurring words in the list
# together with their frequency of occurrence.
# The output should be sorted in descending order by frequency of occurrence.
# If two words occur with the same frequency then they should be ordered in alphabetical order.
# Input:
#
# N = 3
# list = united, states, america, north, america, south, america, south, africa, north, korea
#
# Output:
#
# 3 america
# 2 north
# 2 south
from collections import Counter


def most_frequent(words, n):
    return sorted(Counter(words).most_common(n))


def test_most_frequent():
    assert most_frequent(['apple', 'banana', 'apple', 'yeti'], 2) == [('apple', 2), ('banana', 1)]


def test_most_frequent_same_frequency():
    assert most_frequent(['banana', 'apple', 'apple', 'banana'], 2) == [('apple', 2), ('banana', 2)]


def test_most_frequent_empty():
    assert most_frequent([], 2) == []