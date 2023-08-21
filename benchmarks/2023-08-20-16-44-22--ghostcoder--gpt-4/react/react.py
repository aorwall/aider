class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.dependents = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for cell in self.dependents:
            cell.compute_value()

    def add_dependent(self, cell):
        self.dependents.append(cell)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self._value = None  # Initialize _value before calling compute_value
        for cell in inputs:
            cell.add_dependent(self)
        self.compute_value()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        if old_value != new_value:
            for callback in self.callbacks:
                callback(new_value)

    def compute_value(self):
        self.value = self.compute_function([cell.value for cell in self.inputs])

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)