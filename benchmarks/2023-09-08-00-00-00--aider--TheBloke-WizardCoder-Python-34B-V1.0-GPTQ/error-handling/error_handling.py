class FileLike:
    def __init__(self):
        self.is_open = False

    def open(self):
        if self.is_open:
            raise Exception("File is already open")
        self.is_open = True

    def close(self):
        if not self.is_open:
            raise Exception("File is already closed")
        self.is_open = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def do_something(self):
        if not self.is_open:
            raise Exception("File is not open")
        # do something here

def handle_error_by_throwing_exception():
    raise Exception("An error occurred")

def handle_error_by_returning_none(arg):
    return None

def handle_error_by_returning_tuple(arg):
    return True, arg

def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except Exception as e:
        pass
    assert filelike_object.was_open is False
