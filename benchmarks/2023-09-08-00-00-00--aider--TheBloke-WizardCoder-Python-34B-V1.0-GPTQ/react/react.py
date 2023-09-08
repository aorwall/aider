class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)