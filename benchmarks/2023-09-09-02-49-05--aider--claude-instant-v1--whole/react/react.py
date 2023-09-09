class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            self._call_callbacks()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def _call_callbacks(self):
        for callback in self.callbacks:
            callback()


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = None
        self.callbacks = []

    def recompute(self):
        input_values = [cell.value for cell in self.inputs]
        new_value = self.compute_function(*input_values)
        if self.value != new_value:
            self.value = new_value
            for callback in self.callbacks:
                callback()

    def add_callback(self, callback):
        self.callbacks.append(callback)
