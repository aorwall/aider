class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []

    def set_value(self, new_value):
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
        self.value = None
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

    def update(self):
        new_value = self.compute_function(self.inputs)
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)
    