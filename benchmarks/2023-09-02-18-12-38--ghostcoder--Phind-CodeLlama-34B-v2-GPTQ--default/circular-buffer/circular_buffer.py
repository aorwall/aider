import collections
from typing import Optional
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


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = collections.deque(maxlen=capacity)

    def read(self):
        if len(self._buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        return self._buffer.popleft()

    def write(self, data):
        if len(self._buffer) == self._capacity:
            raise BufferFullException("Circular buffer is full")
        self._buffer.append(data)

    def overwrite(self, data):
        if len(self._buffer) < self._capacity:
            self._buffer.append(data)
        else:
            self._buffer.popleft()
            self._buffer.append(data)

    def clear(self):
        while self._buffer:
            self._buffer.popleft()
