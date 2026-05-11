import os
import json
from datetime import datetime, timezone
import fcntl

class BaseMemoryLayer:
    """Base class for memory layers. Provides safe access to the Registry."""
    def __init__(self, workspace_root):
        self.workspace_root = workspace_root
        self.registry_path = os.path.join(workspace_root, "meta_management/registry.json")

    def _get_utc_now(self):
        """Returns ISO format timestamp with UTC Z suffix."""
        return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    def update_registry(self, update_func):
        """
        Safely reads, updates, and saves the registry using file locking.
        """
        if not os.path.exists(self.registry_path):
            print(f"Registry not found at {self.registry_path}. Skipping update.")
            return

        with open(self.registry_path, 'r+') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                data = json.load(f)
                updated_data = update_func(data)
                updated_data["last_updated"] = self._get_utc_now()
                
                f.seek(0)
                json.dump(updated_data, f, indent=2)
                f.truncate()
            except json.JSONDecodeError:
                print("Error: registry.json is corrupted.")
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
