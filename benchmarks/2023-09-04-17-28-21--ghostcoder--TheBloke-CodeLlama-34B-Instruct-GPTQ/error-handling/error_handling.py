import traceback
from typing import Optional


def handle_error_by_throwing_exception():
    raise Exception("Error message")


def handle_error_by_returning_none(input_data):
    try:
        # Some logic that might fail
        return int(input_data) / 0
    except ValueError:
        return None
    except ZeroDivisionError:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        # Some logic that might fail
        return (int(input_data) / 0,)
    except ValueError:
        return (None, "ValueError occurred.")
    except ZeroDivisionError:
        return (None, "Zero division error occurred.")


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        # Some logic that might fail
        filelike_object.do_something()
    finally:
        filelike_object.close()
