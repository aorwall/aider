class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    
    message: explanation of the error.
    
    """
    def __init__(self, message="Buffer is already full"):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    
    message: explanation of the error.
    
    """
    def __init__(self, message="Buffer is empty"):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self._capacity = capacity
        self._data = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def _increment(self, pointer):
        return (pointer + 1) % self._capacity


    def read(self):
        if self._size == 0:
            raise BufferEmptyException()
        value = self._data[self._head]
        self._head = self._increment(self._head)
        self._size -= 1
        return value


    def write(self, data):
        if self._size >= self._capacity:
            raise BufferFullException()
        self._data[self._tail] = data
        self._tail = self._increment(self._tail)
        self._size += 1


    def overwrite(self, data):
        self._data[self._tail] = data
        self._tail = self._increment(self._tail)
        if self._size < self._capacity:
            self._size += 1


    def clear(self):
        self._head = 0
        self._tail = 0
        self._size = 0
