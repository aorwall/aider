import collections

class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._observers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._notify()

    def _notify(self):
        for observer in self._observers:
            observer()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._inputs = inputs
        self._compute_function = compute_function
        self._value = None
        self._observers = []
        self._dependencies = set()

        # Set up dependencies between inputs and this cell
        for input_cell in self._inputs:
            input_cell.add_observer(self._update)
            self._dependencies.add(input_cell)

    @property
    def value(self):
        return self._value

    def _update(self):
        old_value = self._value
        self._value = self._compute_function(*[input_cell.value for input_cell in self._inputs])
        if self._value != old_value:
            self._notify()

    def _notify(self):
        for observer in self._observers:
            observer()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def remove_dependency(self, dependency):
        self._dependencies.discard(dependency)

    def clear_dependencies(self):
        self._dependencies = set()

    def get_dependencies(self):
        return list(self._dependencies)

    def __repr__(self):
        return f"ComputeCell({self._inputs}, {self._compute_function})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    