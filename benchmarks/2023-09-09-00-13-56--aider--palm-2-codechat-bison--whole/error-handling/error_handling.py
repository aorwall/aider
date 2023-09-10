def handle_error_by_throwing_exception():
    raise Exception("This is an error")


def handle_error_by_returning_none(input_data):
    if input_data == "error":
        return None
    else:
        return input_data


def handle_error_by_returning_tuple(input_data):
    if input_data == "error":
        return (None, None)
    else:
        return (input_data, input_data)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except Exception:
        pass

    self.assertIs(filelike_object.was_open, False,
                  "filelike_object should have been closed")
