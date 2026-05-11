import sys
import os

# Add current directory to path so we can import the modules
sys.path.append(os.getcwd())

from meta_management.l1_manager import L1Manager
from meta_management.l2_archiver import L2Archiver
from meta_management.l3_theorist import L3Theorist

def test_recovery_and_update():
    WORKSPACE_ROOT = "/home/tack-mit/デスクトップ/Gemini_projectspace"
    
    print("=== Testing Meta-Management Refactoring ===\n")
    
    # 1. Test L1 Recovery
    print("[Testing L1 Recovery...]")
    l1 = L1Manager(WORKSPACE_ROOT)
    summary = l1.get_state_summary()
    print(f"Summary Length: {len(summary)} characters (Expected non-zero)")
    print(f"Summary Start: {summary.splitlines()[0] if summary else 'EMPTY'}")
    assert len(summary) > 0, "L1 Summary should not be empty"
    print("L1 OK.\n")
    
    # 2. Test L2 Archiving (Atomic Update)
    print("[Testing L2 Archiving...]")
    l2 = L2Archiver(WORKSPACE_ROOT)
    l2.archive_phase(
        phase_id="Phase_Test_Refactor", 
        category="Management Test", 
        report_path="internal/test.md", 
        summary="Verifying BaseMemoryLayer sync."
    )
    print("L2 OK.\n")
    
    # 3. Test L3 Theoretical Anchoring
    print("[Testing L3 Theorist...]")
    l3 = L3Theorist(WORKSPACE_ROOT)
    l3.register_scientific_law(
        name="Refactoring_Is_Good", 
        description="A law stating that clean code improves AI memory."
    )
    print("L3 OK.\n")
    
    print("=== All Tests Passed (Integration Level) ===")

if __name__ == "__main__":
    test_recovery_and_update()
