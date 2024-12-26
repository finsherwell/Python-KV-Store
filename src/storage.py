from io import BytesIO
import msgpack
from persistence import Persistance

class Storage():
    def __init__(self):
        self.stream = BytesIO()
        self.data = {}
        self.persistance = Persistance(True, True)
    
    def _sync_with_stream(self):
        """Helper function to sync data with BytesIO stream."""
        self.stream.seek(0)
        self.stream.write(msgpack.packb(self.data))
        self.stream.flush()
    
    def set(self, data) -> bool:
        """Store key-value pair in memory, persistence logs command."""
        pass

    def get(self, key):
        """Get value for a specific key."""
        pass
    
    def delete(self, key) -> bool:
        """Delete a key-value pair."""
        pass
    
    def flush(self) -> bool:
        """Clear all data in the memory store and stream."""
        pass
    
    def mset(self, *items) -> bool:
        """Set multiple key-value pairs at once."""
        pass
    
    def mget(self, *keys):
        """Return multiple values for the given keys."""
        pass

    def load_persistence(self):
        """Load data from persistence (if any)."""