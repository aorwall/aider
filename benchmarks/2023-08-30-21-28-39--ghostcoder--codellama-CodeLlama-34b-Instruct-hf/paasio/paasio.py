import io


class MeteredFile(io.BufferedRandom):

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
        pass

    def read(self, size=-1):
        data = super().read(size)
        self.read_bytes += len(data)
        self.read_ops += 1
        return data

    @property
    def read_bytes(self):
        return self.read_bytes

    @property
    def read_ops(self):
        return self.read_ops

    def write(self, b):
        super().write(b)
        self.write_bytes += len(b)
        self.write_ops += 1

    @property
    def write_bytes(self):
        return self.write_bytes

    @property
    def write_ops(self):
        return self.write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.socket = socket
        self.recv_bytes = 0
        self.recv_ops = 0
        self.send_bytes = 0
        self.send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def recv(self, bufsize, flags=0):
        data = self.socket.recv(bufsize, flags)
        self.recv_bytes += len(data)
        self.recv_ops += 1
        return data

    @property
    def recv_bytes(self):
        return self.recv_bytes

    @property
    def recv_ops(self):
        return self.recv_ops

    def send(self, data, flags=0):
        self.socket.send(data, flags)
        self.send_bytes += len(data)
        self.send_ops += 1

    @property
    def send_bytes(self):
        return self.send_bytes

    @property
    def send_ops(self):
        return self.send_ops
