import collections
from typing import Union

class BufferFullException(Exception):
    """Exception raised when CircularBuffer is full.
    
    message: explanation of the error.
    
    """
    def __init__(self, message="Circular buffer is full."):
        super().__init__(message)


class BufferEmptyException(Exception):
    """Exception raised when CircularBuffer is empty.
    
    message: explanation of the error.
    
    """
    def __init__(self, message="Circular buffer is empty."):
        super().__init__(message)

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
        self._deque = collections.deque([], maxlen=capacity)

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return len(self._deque)

    def read(self):
        try:
            return self._deque.popleft()
        except IndexError as err:
            raise BufferEmptyException from err

    def write(self, data):
        if self.size >= self.capacity:
            raise BufferFullException
        self._deque.append(data)

    def overwrite(self, data):
        if self.size < self.capacity:
            self._deque.append(data)
        else:
            self._deque.popleft()
            self._deque.append(data)

    def clear(self):
        self._deque.clear()
