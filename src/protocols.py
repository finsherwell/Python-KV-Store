class ProtocolHandler:
    def __init__(self):
        self.handlers = {
            '#': self.simple_string,
            '~': self.error,
            '%': self.integer,
            '&': self.bulk_string,
            '@': self.array,
            '$': self.dict
        }
    
    def simple_string(self):
        pass

    def error(self):
        pass

    def integer(self):
        pass

    def bulk_string(self):
        pass

    def array(self):
        pass

    def dict(self):
        pass