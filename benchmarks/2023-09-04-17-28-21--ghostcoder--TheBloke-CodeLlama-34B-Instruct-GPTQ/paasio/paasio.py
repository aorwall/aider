import io
from contextlib import contextmanager

@contextmanager
def metered_socket(socket):
    # Implementation details here
    yield None

class MeteredFile(io.BufferedRandom):
    def __init__(self, fp, mode='r', buffering=-1, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False):
        super().__init__(fp, mode, buffering, encoding, errors, newline, line_buffering, write_through)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def _read(self, size=-1):
        chunk = super()._read(size)
        self._read_bytes += len(chunk)
        self._read_ops += 1
        return chunk

    def _write(self, data):
        written = super()._write(data)
        self._write_bytes += written
        self._write_ops += 1
        return written

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def recv(self, bufsize, flags=0):
        pass

    @property
    def recv_bytes(self):
        pass

    @property
    def recv_ops(self):
        pass

    def send(self, data, flags=0):
        pass

    @property
    def send_bytes(self):
        pass

    @property
    def send_ops(self):
        pass
