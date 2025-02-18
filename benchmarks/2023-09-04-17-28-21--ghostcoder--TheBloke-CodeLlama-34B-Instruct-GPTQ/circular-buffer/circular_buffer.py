class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    
    message: explanation of the error.
    
    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    
    message: explanation of the error.
    
    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = []
        self._head = -1
        self._tail = -1

    def read(self):
        if len(self._data) == 0:
            raise BufferEmptyException("No data left to read.")
        else:
            result = self._data[self._head]
            self._head += 1
            return result

    def write(self, data):
        if len(self._data) < self._capacity:
            self._data.append(data)
            self._tail += 1
        elif len(self._data) >= self._capacity:
            raise BufferFullException("Cannot add data; buffer is already at maximum capacity.")

    def overwrite(self, data):
        if len(self._data) < self._capacity:
            self._data.insert(0, data)
            self._tail += 1
        elif len(self._data) >= self._capacity:
            self._data.pop()
            self._data.insert(0, data)
            self._tail += 1

    def clear(self):
        self._data = []
        self._head = -1
        self._tail = -1
