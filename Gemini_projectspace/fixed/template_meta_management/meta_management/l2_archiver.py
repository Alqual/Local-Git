from meta_management.memory_base import BaseMemoryLayer
import os

class L2Archiver(BaseMemoryLayer):
    """Manages the Episodic Memory Layer (L2) and Phase Settlement."""
    def __init__(self, workspace_root):
        super().__init__(workspace_root)

    def archive_phase(self, phase_id, category, report_path, summary):
        """Registers a completed/scrutinized phase into the episodic index."""
        
        def _update(data):
            new_episode = {
                "phase": phase_id,
                "category": category,
                "report": report_path,
                "summary": summary,
                "status": "Archived",
                "timestamp": self._get_utc_now()
            }
            data["layers"]["l2_episodic"]["index"].insert(0, new_episode)
            return data

        self.update_registry(_update)
        print(f"L2: Phase {phase_id} archived.")

if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    archiver = L2Archiver(root)
    print("L2 Archiver initialized at", root)
