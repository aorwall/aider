class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []
        
    def set_value(self, new_value):
        self.value = new_value
        for callback in self.callbacks:
            callback(self)
            
class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = None
        self.callbacks = []
        
        for input in inputs:
            input.callbacks.append(self.recompute)
            
        self.recompute()
            
    def add_callback(self, callback):
        self.callbacks.append(callback)
        
    def remove_callback(self, callback):
        self.callbacks.remove(callback)
        
    def recompute(self, changed_input=None):
        input_values = [input.value for input in self.inputs]
        new_value = self.compute_function(input_values)
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self)
