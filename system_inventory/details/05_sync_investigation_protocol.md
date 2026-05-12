# Multi-Node Sync Investigation Protocol

This protocol defines the standard procedure for an agent to investigate synchronization states between local environments (e.g., Alma Linux, Ubuntu) and the remote Single Source of Truth (GitHub) without requiring explicit user approval for the investigation steps.

## Purpose
To accurately determine "who has what" and "where the latest version is" when multiple nodes are contributing to the same repository.

## Procedure

### 1. Local & Remote Parity Check
First, verify if the local branch is tracking the correct remote and check the commit history.
```bash
# Check current branch and tracking status
git status

# Fetch latest remote state without merging
git fetch origin

# Compare commit hashes of local and remote
git log -n 5 --oneline HEAD
git log -n 5 --oneline origin/<current_branch>
```

### 2. Physical File Existence Check
Check for untracked files that might contain "orphan" work not yet committed.
```bash
# List untracked files/directories
git status # (Look at "Untracked files" section)

# Check timestamps of untracked assets to confirm "freshness"
ls -ld <directory_name>
```

### 3. Remote Content Verification
Confirm if specific files/directories exist in the remote history (to detect if they were deleted or pushed from another node).
```bash
# List files in the latest remote commit
git ls-tree -r origin/<current_branch> --name-only | grep <keyword>

# Search entire history for a specific filename if it seems "lost"
git rev-list --all | xargs git grep "<filename>"
```

### 4. Cross-Branch Inspection
If the expected content isn't in the current branch, check other active branches.
```bash
# List all branches
git branch -a

# Check recent activity on other remotes
git log -n 5 --oneline origin/Mains
git log -n 5 --oneline origin/Git-Con
```

## Safety Assessment
This investigation protocol consists entirely of **Read-Only** operations (`git status`, `fetch`, `log`, `ls-tree`, `ls`). It does not modify the filesystem or the git index, making it safe for autonomous execution by agents to provide situational awareness.
