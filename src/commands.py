class CommandError(Exception): pass

class Command:
    def __init__(self, storage):
        self.storage = storage
        self.commands = self.get_commands()
    
    def get_commands(self):
        return {
            "SET": self.storage.set,
            'GET': self.storage.get,
            'DELETE': self.storage.delete,
            'FLUSH': self.storage.flush,
            'MSET': self.storage.mset,
            'MGET': self.storage.mget
        }
    
    def respond(self, data):
        if not isinstance(data, list):
            try:
                data = data.split()
            except:
                raise CommandError('Request must be list or simple string!')
        if not data:
            raise CommandError('Missing command')
        
        command = data[0].upper()
        if command not in self.commands:
            raise CommandError('Unrecognized command: %s' % command)

        return self.commands[command](*data[1:])