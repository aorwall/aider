import io
from functools import wraps


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, fp, *args, **kwargs):
        super().__init__(fp)
        self._read_bytes = 0
        self._write_bytes = 0
        self._read_ops = 0
        self._write_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __iter__(self):
        return iter(self.readline, '')

    def _update_read_stats(self, n):
        if n > 0:
            self._read_bytes += n
            self._read_ops += 1

    def read(self, size=-1):
        chunk = super().read(size)
        self._update_read_stats(len(chunk))
        return chunk

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops


    def _update_write_stats(self, n):
        if n > 0:
            self._write_bytes += n
            self._write_ops += 1

    def write(self, b):
        bytes_written = super().write(b)
        self._update_write_stats(len(b))
        return bytes_written

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops



class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, sock):
        self._sock = sock
        self._recv_bytes = 0
        self._send_bytes = 0
        self._recv_ops = 0
        self._send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def recv(self, bufsize, flags=0):
        chunk = self._sock.recv(bufsize, flags)
        self._recv_bytes += len(chunk)
        self._recv_ops += 1
        return chunk

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops


    def send(self, data, flags=0):
        bytes_sent = self._sock.send(data, flags)
        self._send_bytes += bytes_sent
        self._send_ops += 1
        return bytes_sent

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops
