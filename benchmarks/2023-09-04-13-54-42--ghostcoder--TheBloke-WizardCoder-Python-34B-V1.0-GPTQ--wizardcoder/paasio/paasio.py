import io
from functools import wraps


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line

    def _update_read_stats(self, size):
        self._read_bytes += size
        self._read_ops += 1

    def _update_write_stats(self, size):
        self._write_bytes += size
        self._write_ops += 1

    def read(self, size=-1):
        data = super().read(size)
        self._update_read_stats(len(data))
        return data

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        num_bytes = len(b)
        super().write(b)
        self._update_write_stats(num_bytes)

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _update_recv_stats(self, data):
        self._recv_bytes += len(data)
        self._recv_ops += 1

    def _update_send_stats(self, size):
        self._send_bytes += size
        self._send_ops += 1

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize, flags)
        self._update_recv_stats(data)
        return data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        size = self._socket.send(data, flags)
        self._update_send_stats(size)
        return size

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops
