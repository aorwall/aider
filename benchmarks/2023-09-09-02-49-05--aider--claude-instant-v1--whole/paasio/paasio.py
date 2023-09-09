import io
import sys

class MeteredFile(io.BufferedRandom):

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
        pass

    def __next__(self):
        pass

    def read(self, size=-1):
        self._read_ops += 1
        data = super().read(size)
        self._read_bytes += len(data)
        return data

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        self._write_ops += 1
        self._write_bytes += len(b)
        return super().write(b)

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:

    def __init__(self, socket):
        self.socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def recv(self, bufsize, flags=0):
        self._recv_ops += 1 
        data = self.socket.recv(bufsize, flags)
        self._recv_bytes += len(data)
        return data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        self._send_ops += 1
        self._send_bytes += len(data)
        return self.socket.send(data, flags)

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def