# https://sites.google.com/site/tddproblems/all-problems-1/recent-file-list
# A popular feature of graphical editors of
# all kinds (text, graphics, spreadsheets, ..) is the Recent file list. It is often found as a sub-menu of the file
# menu in the GUI of the program.
#
# Use TDD to grow this kind of behaviour. Some examples of the behaviour is
#
# When the program is run for the first time, the list is empty When a file is opened, it is added to the recent file
# list If an opened file already exists in the recent file list, it is bumped to the top, not duplicated in the list
# If the recent file list gets full (typical number of items is 15), the oldest item is removed when a new item is
# added
from collections import Counter


class Program:
    _recent_file_list = []

    def __init__(self):
        self._recent_file_list = []

    def open(self, file):
        self._recent_file_list.append(file)
        self._recent_file_list = list(sorted(Counter(self._recent_file_list)))
        return self

    def get_recent_file_list(self):
        return self._recent_file_list


def test_empty_list():
    file_list = Program().get_recent_file_list()
    assert len(file_list) == 0


def test_not_empty_list():
    file_list = Program().open('somefile.txt').get_recent_file_list()
    assert len(file_list) == 1


def test_bumping_item():
    program = Program()

    program.open('2.txt')
    program.open('1.txt')
    program.open('1.txt')

    file_list = program.get_recent_file_list()
    assert file_list[0] == '1.txt'


def test_item_should_not_be_duplicated():
    program = Program()

    program.open('1.txt')
    program.open('1.txt')

    file_list = program.get_recent_file_list()
    assert len(file_list) == 2
