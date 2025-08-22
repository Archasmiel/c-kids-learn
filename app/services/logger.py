from flask import Flask


class Logger:
    @staticmethod
    def msg(cause: str, s: str):
        print(f'[{cause}]> {s}')

    def info(self, s: str):
        self.msg('Info   ', s)

    def warning(self, s: str):
        self.msg('Warning', s)

    def error(self, s: str):
        self.msg('Error  ', s)

    def backup(self, s: str):
        self.msg('Backup ', s)


logger = Logger()


def register(app: Flask):
    pass
