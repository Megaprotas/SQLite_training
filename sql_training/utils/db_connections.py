import sqlite3


class DatabaseConnection(object):
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_trace):
        if exc_type or exc_val or exc_trace:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()