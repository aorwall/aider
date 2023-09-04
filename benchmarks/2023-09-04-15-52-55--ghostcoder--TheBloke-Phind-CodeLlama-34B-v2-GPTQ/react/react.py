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
        for observer in self._observers:
            observer()


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._inputs = inputs
        self._compute_function = compute_function
        self._value = None
        self._callbacks = []

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        self._callbacks.remove(callback)

    def _recalculate(self):
        new_value = self._compute_function([input_cell.value for input_cell in self._inputs])
        if new_value != self._value:
            self._value = new_value
            for callback in self._callbacks:
                callback()

    def observe(self):
        for input_cell in self._inputs:
            input_cell._observers.append(self._recalculate)
        self._recalculate()


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


if __name__ == "__main__":
    num1 = InputCell(5)
    num2 = InputCell(3)

    calc = ComputeCell([num1, num2], multiply)

    def print_calc():
        print(f"New calculation: {calc.value}")

    calc.add_callback(print_calc)

    num1.value = 4
    num2.value = 6
    