import collections


class CircularBuffer:
    """A circular buffer that stores data in a first-in, first-out (FIFO)
    manner.

    Args:
        max_size: The maximum number of items that can be stored in the buffer.

    Attributes:
        _data: A list that stores the data in the buffer.
        _head: The index of the first item in the buffer.
        _tail: The index of the next empty slot in the buffer.
    """

    def __init__(self, max_size):
        self._data = collections.deque(maxlen=max_size)
        self._head = 0
        self._tail = 0

    def __len__(self):
        """Returns the number of items currently stored in the buffer."""
        return len(self._data)

    def is_empty(self):
        """Returns True if the buffer is empty."""
        return len(self._data) == 0

    def is_full(self):
        """Returns True if the buffer is full."""
        return len(self._data) == self._max_size

    def append(self, item):
        """Adds an item to the end of the buffer.

        Args:
            item: The item to add to the buffer.

        Raises:
            ValueError: If the buffer is full.
        """
        if self.is_full():
            raise ValueError("Buffer is full")

        self._data.append(item)

    def get(self):
        """Removes and returns the item at the front of the buffer.

        If the buffer is empty, raises a `ValueError` exception.

        Returns:
            The item at the front of the buffer.

        Raises:
            ValueError: If the buffer is empty.
        """
        if self.is_empty():
            raise ValueError("Buffer is empty")

        item = self._data[self._head]
        self._head = (self._head + 1) % self._max_size

        return item

    def clear(self):
        """Clear