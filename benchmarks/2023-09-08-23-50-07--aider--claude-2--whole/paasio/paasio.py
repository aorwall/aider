import io

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_bytes = 0
        self.read_ops = 0
        self.write_bytes = 0 
        self.write_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._reader)

    def read(self, size=-1):
        data = super().read(size)
        self.read_bytes += len(data)
        self.read_ops += 1
        return data

    @property
    def read_bytes(self):
        return self._read_bytes

    @read_bytes.setter
    def read_bytes(self, value):
        self._read_bytes = value

    @property
    def read_ops(self):
        return self._read_ops
    
    @read_ops.setter
    def read_ops(self, value):
        self._read_ops = value

    def write(self, b):
        n = super().write(b)
        self.write_bytes += n
        self.write_ops += 1
        return n

    @property
    def write_bytes(self):
        return self._write_bytes

    @write_bytes.setter
    def write_bytes(self, value):
        self._write_bytes = value

    @property
    def write_ops(self):
        return self._write_ops
    
    @write_ops.setter
    def write_ops(self, value):
        self._write_ops = value


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self.recv_bytes = 0
        self.recv_ops = 0
        self.send_bytes = 0
        self.send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize