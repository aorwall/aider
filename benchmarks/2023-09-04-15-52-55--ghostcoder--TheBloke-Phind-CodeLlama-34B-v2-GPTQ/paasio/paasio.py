import io


class MeteredFile(io.BufferedRandom):
    def __init__(self, fileobj, name='<unknown>'):
        super().__init__(fileobj)
        self._name = name
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r})"

    def read(self, size=-1):
        chunk = super().read(size)
        self._read_bytes += len(chunk)
        self._read_ops += 1
        return chunk

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        written = super().write(b)
        self._write_bytes += written
        self._write_ops += 1
        return written

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    def __init__(self, sock):
        self._sock = sock
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __getattr__(self, attr):
        return getattr(self._sock, attr)

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
        sent = self._sock.send(data, flags)
        self._send_bytes += sent
        self._send_ops += 1
        return sent

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops
