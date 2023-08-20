class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []

    def set_value(self, new_value):
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = self.compute_function([input_cell.value for input_cell in self.inputs])
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

    def update_value(self):
        new_value = self.compute_function([input_cell.value for input_cell in self.inputs])
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)
