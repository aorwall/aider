import functools

class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._observers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            old_value = self._value
            self._value = new_value
            for observer in self._observers:
                observer(old_value, new_value)

    def bind_to(self, observer):
        self._observers.append(observer)

    def unbind_from(self, observer):
        self._observers.remove(observer)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._dependents = {}
        self._value = None
        self._compute_function = compute_function

        for input_cell in inputs:
            input_cell.bind_to(functools.partial(self._update, input_cell))

    def _update(self, changed_input, old_value, new_value):
        self._recalculate()

    def _recalculate(self):
        inputs = [input_cell.value for input_cell in self._dependents]
        self._value = self._compute_function(*inputs)

        for dependent in self._dependents:
            dependent._update(self, self._value)

    def add_callback(self, callback):
        if not hasattr(self, '_callbacks'):
            self._callbacks = []
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        if hasattr(self, '_callbacks') and callback in self._callbacks:
            self._callbacks.remove(callback)

    def connect(self, output):
        self._dependents[output] = True
        if output._value is None:
            output._recalculate()

    def disconnect(self, output):
        del self._dependents[output]


if __name__ == "__main__":
    # Test cases here
    