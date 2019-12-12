from collections import deque


class Program:
    _max_list_length = 15

    def __init__(self):
        self._recent_file_list = deque()

    def open(self, file):
        if file in self._recent_file_list:
            self._recent_file_list.remove(file)
        self._recent_file_list.appendleft(file)
        if len(self._recent_file_list) > self._max_list_length:
            self._recent_file_list.pop()
        return self

    def get_recent_file_list(self):
        return self._recent_file_list
