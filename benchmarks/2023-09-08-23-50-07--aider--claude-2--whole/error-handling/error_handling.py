def handle_error_by_throwing_exception():
    raise ValueError("Error occurred")


def handle_error_by_returning_none(input_data):
    if input_data is None:
        return None
    else:
        return input_data


def handle_error_by_returning_tuple(input_data):
    if input_data is None:
        return (None, "Error occurred")
    else:
        return (input_data, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something() 
    finally:
        filelike_object.close()
