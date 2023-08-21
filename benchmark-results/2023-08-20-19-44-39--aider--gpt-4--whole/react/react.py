class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.dependents = []

    def set_value(self, value):
        self.value = value
        for cell in self.dependents:
            cell.compute()

    def add_dependent(self, cell):
        self.dependents.append(cell)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.value = None
        self.dependents = []
        for cell in inputs:
            cell.add_dependent(self)
        self.compute()

    def compute(self):
        new_value = self.compute_function([input.value for input in self.inputs])
        if new_value != self.value:
            self.value = new_value
            self.call_callbacks()
            for cell in self.dependents:
                cell.compute()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)

    def call_callbacks(self):
        for callback in self.callbacks:
            callback(self.value)

    def add_dependent(self, cell):
        self.dependents.append(cell)
