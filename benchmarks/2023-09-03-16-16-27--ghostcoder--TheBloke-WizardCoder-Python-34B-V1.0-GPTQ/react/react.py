import weakref

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
            for cb in self._callbacks:
                cb()

    def add_callback(self, callback):
        self._callbacks.append(weakref.WeakMethod(callback))

    def remove_callback(self, callback):
        try:
            self._callbacks.remove(weakref.WeakMethod(callback))
        except ValueError:
            pass


class ComputeCell:
    def __init__(self, inputs, func):
        self._inputs = inputs
        self._func = func
        self._value = None
        self._callbacks = []

        # Add callbacks to all input cells so that we can recalculate when they change.
        for cell in self._inputs:
            cell.add_callback(lambda: self.recalc())

        self.recalc()  # calculate our initial value

    def recalc(self):
        values = [c.value for c in self._inputs]
        self._value = self._func(*values)
        for cb in self._callbacks:
            cb()

    def add_callback(self, callback):
        self._callbacks.append(weakref.WeakMethod(callback))

    def remove_callback(self, callback):
        try:
            self._callbacks.remove(weakref.WeakMethod(callback))
        except ValueError:
            pass

    @property
    def value(self):
        return self._value
    