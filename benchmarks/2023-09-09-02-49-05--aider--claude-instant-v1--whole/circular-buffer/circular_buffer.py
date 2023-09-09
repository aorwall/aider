class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""

    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""

    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start_idx = 0
        self.current_idx = 0

    def read(self):
        if self.is_empty():
            raise BufferEmptyException("Buffer is empty")
        data = self.buffer[self.start_idx]
        self.start_idx = (self.start_idx + 1) % self.capacity
        return data

    def write(self, data):
        if self.is_full():
            self._make_space()
        self.buffer[self.current_idx] = data
        self.current_idx = (self.current_idx + 1) % self.capacity

    def _make_space(self):
        for i in range(self.start_idx, self.capacity):
            self.buffer[i-1] = self.buffer[i]
        self.buffer[self.capacity-1] = None
        self.start_idx -= 1
        if self.start_idx < 0:
            self.start_idx += self.capacity

    def is_full(self):
        return self.current_idx == self.start_idx

    def is_empty(self):
        return self.current_idx == self.start_idx

    def clear(self):
        self.buffer = [None] * self.capacity
        self.start_idx = 0
        self.current_idx = 0
