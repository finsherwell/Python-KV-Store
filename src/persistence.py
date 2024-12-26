import os

class Persistance:
    def __init__(self, snapshot, aof):
        self.saved_data = os.getenv('DATA_SNAPSHOT_FILE')
        self.logged_data = os.getenv('DATA_LOGGING_FILE')
    
    def snapshot(interval=10):
        """Takes snapsnots every interval, of the current state of the data, stores on disk."""
        pass

    def aof():
        """Logs commands to the logging file (disk) each time they are made."""
        pass