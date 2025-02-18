import contextlib

@contextlib.contextmanager
def open_file(filelike_object):
    try:
        filelike_object.open()
        yield filelike_object
    finally:
        filelike_object.close()

def handle_error_by_throwing_exception():
    raise Exception('Error occurred')

def handle_error_by_returning_none(input_data):
    try:
        # Some operation on input data
        pass
    except Exception:
        return None

def handle_error_by_returning_tuple(input_data):
    try:
        # Some operation on input data
        pass
    except Exception as e:
        return (None, str(e))

def filelike_objects_are_closed_on_exception(filelike_object):
    with open_file(filelike_object) as f:
        f.do_something()
