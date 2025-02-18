import sys
from typing import Optional, Tuple

class FileLike:
    def open(self):
        print('Opening')

    def do_something(self):
        raise Exception('Error occurred while doing something')

    def close(self):
        print('Closing')

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.close()
        if exc_type is None:
            # No exception was raised
            return True
        else:
            # An exception was raised
            return False


def handle_error_by_throwing_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError('A value error occurred')


def handle_error_by_returning_none(input_data):
    try:
        int(input_data)
    except ValueError:
        return None
    return int(input_data)


def handle_error_by_returning_tuple(input_data):
    try:
        int(input_data)
    except ValueError:
        return (None, 'Invalid input data')
    return (int(input_data), '')


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        with filelike_object as f:
            f.do_something()
    except Exception as e:
        print(f"An exception occurred: {e}")
        sys.exit(1)
