class FileLike:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def handle_error_by_throwing_exception():
    raise Exception("This is an error")


def handle_error_by_returning_none(input_data):
    if input_data == "":
        return None
    else:
        return input_data


def handle_error_by_returning_tuple(input_data):
    try:
        result = int(input_data)
        return (result,)
    except ValueError:
        return (None,)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except Exception:
        filelike_object.close()
        raise
