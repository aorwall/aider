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
        self.start = 0
        self.end = 0

    def read(self):
        if self.buffer[self.start] is None:
            raise BufferEmptyException
        data = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.capacity
        return data

    def write(self, data):
        if self.buffer[self.end] is not None:
            raise BufferFullException
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.capacity

    def overwrite(self, data):
        if self.buffer[self.end] is None:
            self.write(data)
        else:
            self.buffer[self.end] = data
            self.end = (self.end + 1) % self.capacity
            if self.buffer[self.start] is not None:
                self.start = (self.start + 1) % self.capacity

    def clear(self):
        self.buffer = [None]*self.capacity
        self.start = 0
        self.end = 0
