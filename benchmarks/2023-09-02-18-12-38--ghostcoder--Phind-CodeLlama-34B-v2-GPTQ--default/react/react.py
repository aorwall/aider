class InputCell:
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        if self._value != new_val:
            self._value = new_val
            for callback in self._callbacks:
                callback(new_val)  # Pass the new value to the callback function

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._inputs = inputs
        self._compute_function = compute_function
        self._value = None
        self._callbacks = []
        self.recalculate()  # Sets an initial value

        for input_cell in inputs:
            input_cell.add_callback(self.recalculate)

    def recalculate(self, *args):
        new_val = self._compute_function([input_cell.value for input_cell in self._inputs])
        if self._value != new_val:
            self._value = new_val
            for callback in self._callbacks:
                callback(self._value)  # Pass the new value to the callback function

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
    