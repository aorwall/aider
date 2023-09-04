class InputCell:
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if v != self._value:
            self._value = v
            self.notify()

    def notify(self):
        for callback in self._callbacks:
            callback(self)

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

        # Subscribe to input cells
        for cell in self._inputs:
            cell.add_callback(self.on_input_change)

        # Initial computation
        self.recompute()

    def on_input_change(self, changed_cell):
        self.recompute()

    def recompute(self):
        new_value = self._compute_function([cell.value for cell in self._inputs])
        if new_value != self._value:
            self._value = new_value
            self.notify()

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def notify(self):
        for callback in self._callbacks:
            callback(self)
    