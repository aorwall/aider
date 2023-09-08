class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0

    def append(self, data):
        if self.is_full():
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity

    def remove(self):
        if self.is_empty():
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        return data

    def is_empty(self):
        return self.buffer.count(None) == self.capacity

    def is_full(self):
        return self.buffer.count(None) == 0

class BufferFullException(Exception):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

class BufferEmptyException(Exception):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
