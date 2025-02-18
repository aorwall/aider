class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    
    message: explanation of the error.
    
    """
    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    
    message: explanation of the error.
    
    """
    def __init__(self, message):
        super().__init__(message)


from collections import deque


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = deque()

    def read(self):
        if len(self._data) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        return self._data.popleft()

    def write(self):
        if len(self._data) >= self._capacity:
            raise BufferFullException("Circular buffer is full.")
        # Add your implementation here

    def overwrite(self, data):
        if len(self._data) < self._capacity:
            self.write(data)
        else:
            self._data.popleft()
            self._data.append(data)

    def clear(self):
        while len(self._data) > 0:
            self._data.popleft()
