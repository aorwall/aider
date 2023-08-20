class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message="Circular buffer is full"):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message="Circular buffer is empty"):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None]*capacity
        self.start = 0
        self.end = 0
        self.is_full = False

    def read(self):
        if self.start == self.end and not self.is_full:
            raise BufferEmptyException
        data = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % len(self.buffer)
        self.is_full = False
        return data

    def write(self, data):
        if self.is_full:
            raise BufferFullException
        self.buffer[self.end] = data
        self.end = (self.end + 1) % len(self.buffer)
        if self.end == self.start:
            self.is_full = True

    def overwrite(self, data):
        self.buffer[self.end] = data
        self.end = (self.end + 1) % len(self.buffer)
        if self.is_full:
            self.start = (self.start + 1) % len(self.buffer)
        if self.end == self.start:
            self.is_full = True

    def clear(self):
        self.buffer = [None]*len(self.buffer)
        self.start = 0
        self.end = 0
        self.is_full = False