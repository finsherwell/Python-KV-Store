class CommandHandler:
    def __init__(self, storage):
        self.storage = storage
    
    def handle_command(self, command, *args) -> bool:
        if command == "SET":
            print("s")
        if command == "GET":
            print("s")
        if command == "DELETE":
            print("s")
        if command == "FLUSH":
            print("s")
        if command == "MSET": # set multiple
            print("s")
        if command == "MGET": # get multiple
            print("s")