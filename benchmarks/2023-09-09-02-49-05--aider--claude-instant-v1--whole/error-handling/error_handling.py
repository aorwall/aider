import traceback

def handle_error_by_throwing_exception():
    raise Exception("An error occurred")


def handle_error_by_returning_none(input_data):
    try:
        return input_data
    except:
        return None


def handle_error_by_returning_tuple(input_data):
    try: 
        return (True, input_data)
    except:
        return (False, "Error message")


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        filelike_object.close()
