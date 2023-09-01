def handle_error_by_throwing_exception():
    raise Exception("This exception is expected")


def handle_error_by_returning_none(input_data):
    if input_data == "invalid_data":
        return None
    return input_data


def handle_error_by_returning_tuple(input_data):
    if input_data == "invalid_data":
        return (None, "Invalid input")
    return (input_data, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
    except Exception:
        filelike_object.close()
    finally:
        filelike_object.close()
