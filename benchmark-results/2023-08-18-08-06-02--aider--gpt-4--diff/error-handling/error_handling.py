def handle_error_by_throwing_exception():
    raise Exception("Exception raised")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return True, int(input_data)
    except ValueError:
        return False, input_data


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
    except Exception:
        filelike_object.close()
        raise
    else:
        filelike_object.close()
