class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message="Circular buffer is full"):
        self.message = message
        super().__init__(self.message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message="Circular buffer is empty"):
        self.message = message
        super().__init__(self.message)


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None]*capacity
        self.capacity = capacity
        self.position = 0

    def read(self):
        value = self.buffer[self.position]
        self.buffer[self.position] = None
        self.position = (self.position + 1) % self.capacity
        return value if value is not None else None

    def write(self, data):
        self.buffer[self.position] = data
        self.position = (self.position + 1) % self.capacity

    def overwrite(self, data):
        self.buffer[self.position] = data
        self.position = (self.position + 1) % self.capacity

    def clear(self):
        self.buffer = [None]*self.capacity
        self.position = 0
