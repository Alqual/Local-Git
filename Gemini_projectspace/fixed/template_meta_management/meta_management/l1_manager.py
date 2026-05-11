from meta_management.memory_base import BaseMemoryLayer
from itertools import islice
import os

class L1Manager(BaseMemoryLayer):
    """Manages the Working Memory Layer (L1) and RESEARCH_STATE.md."""
    def __init__(self, workspace_root):
        super().__init__(workspace_root)
        self.state_file = os.path.join(workspace_root, "RESEARCH_STATE.md")

    def get_state_summary(self):
        """Reads the current state summary efficiently."""
        if not os.path.exists(self.state_file):
            return "No RESEARCH_STATE.md found."
        
        with open(self.state_file, 'r') as f:
            lines = list(islice(f, 20)) # Read more lines in template
        return "".join(lines)

    def update_session_id(self, session_id):
        """Placeholder for updating session ID in RESEARCH_STATE.md."""
        print(f"L1: Session update to {session_id} requested.")

if __name__ == "__main__":
    # Detect workspace root if running directly
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    manager = L1Manager(root)
    print("--- L1 State Summary ---")
    print(manager.get_state_summary())
