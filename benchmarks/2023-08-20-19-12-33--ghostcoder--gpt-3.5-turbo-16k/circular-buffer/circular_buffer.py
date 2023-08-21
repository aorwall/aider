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
        self.capacity = capacity
        self.buffer = []
        self.read_index = 0
        self.write_index = 0

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.read_index]
        self.read_index = (self.read_index + 1) % self.capacity
        return data

    def write(self, data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer[self.write_index] = data
            self.write_index = (self.write_index + 1) % self.capacity
            self.read_index = self.write_index
        else:
            self.write(data)

    def clear(self):
        self.buffer = []
        self.read_index = 0
        self.write_index = 0