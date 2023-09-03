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
            old_val = self._value
            self._value = new_val
            for cb in self._callbacks:
                cb()

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        self._callbacks.remove(callback)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._inputs = inputs
        self._compute_function = compute_function
        self._value = None
        self._callbacks = []
        self._stale = True

        for input_cell in self._inputs:
            input_cell.add_callback(self._mark_as_stale)

    def _mark_as_stable(self):
        self._stale = False

    def _mark_as_stale(self):
        self._stale = True

    @property
    def value(self):
        if self._stale:
            values = [input_cell.value for input_cell in self._inputs]
            self._value = self._compute_function(*values)
            self._stale = False
            for callback in self._callbacks:
                callback()
        return self._value

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        self._callbacks.remove(callback)
    