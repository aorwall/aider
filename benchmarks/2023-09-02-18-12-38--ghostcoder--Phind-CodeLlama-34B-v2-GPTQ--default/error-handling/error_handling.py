class FileLike:
    def __init__(self):
        self._is_open = False

    def open(self):
        self._is_open = True

    def close(self):
        self._is_open = False

    def do_something(self):
        if self._is_open:
            raise Exception("An exception occurred.")

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
def handle_error_by_throwing_exception():
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught an error: {e}")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def handle_error_by_returning_tuple(input_data):
    successful_result = False
    result = (None, "Invalid input")
    try:
        value = int(input_data)
        successful_result = True
        result = (value, "success")
    except ValueError as e:
        print(f"Invalid input: {e}")
    finally:
        return result


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as f:
        try:
            f.do_something()
        except Exception as e:
            print(f"Caught an error: {e}")
