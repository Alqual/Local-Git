from meta_management.memory_base import BaseMemoryLayer
from itertools import islice
import os

class L1Manager(BaseMemoryLayer):
    """Manages the Working Memory Layer (L1) and RESEARCH_STATE.md."""
    def __init__(self, workspace_root):
        super().__init__(workspace_root)
        self.state_file = os.path.join(workspace_root, "RESEARCH_STATE.md")

    def get_state_summary(self):
        """Reads the current state from RESEARCH_STATE.md efficiently."""
        if not os.path.exists(self.state_file):
            return "No RESEARCH_STATE.md found."
        
        # Read only the first 10 lines without loading the whole file
        with open(self.state_file, 'r') as f:
            lines = list(islice(f, 10))
        return "".join(lines)

    def update_session_id(self, session_id):
        """Updates the session ID in RESEARCH_STATE.md (Placeholder integration)."""
        print(f"L1: Updating session to {session_id} in {self.state_file}...")

if __name__ == "__main__":
    manager = L1Manager("/home/tack-mit/デスクトップ/Gemini_projectspace")
    print("--- L1 State Summary ---")
    print(manager.get_state_summary())
