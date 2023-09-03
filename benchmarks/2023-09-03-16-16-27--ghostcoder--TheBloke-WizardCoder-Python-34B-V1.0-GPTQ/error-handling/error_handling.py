import sys
from typing import Tuple


class FileLike:
    def __init__(self):
        self._is_opened = False

    def open(self):
        self._is_opened = True

    def do_something(self):
        raise Exception("Something went wrong")


    def close(self):
        self._is_opened = False

    @property
    def closed(self):
        return not self._is_opened



def handle_error_by_throwing_exception():
    try:
        1 / 0  # this raises ZeroDivisionError
    except ZeroDivisionError:
        print('ZeroDivisionError occurred')
        sys.exit()



def handle_error_by_returning_none(input_data):
    try:
        int('notaninteger')
    except ValueError:
        return None
    else:
        return int(input_data)


def handle_error_by_returning_tuple(input_data):
    try:
        int('notaninteger')
    except ValueError:
        return (True, 'Valid input')
    else:
        return (False, 'Invalid input data')


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        with filelike_object as f:
            f.do_something()
    except Exception:
        pass
    finally:
        assert filelike_object.closed == True
    assert filelike_object.closed == True
