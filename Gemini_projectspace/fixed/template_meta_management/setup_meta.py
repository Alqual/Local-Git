import os
import shutil
import json
from datetime import datetime, timezone
import sys

def setup_meta(target_dir, project_name):
    # Template source path (relative to this script)
    template_src = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Initializing 3-Layer Meta-Management for: {project_name}")
    print(f"Target Directory: {target_dir}")

    # Paths to exclude (the setup script itself and git if present)
    exclude = ['setup_meta.py', '.git', '__pycache__']

    # 1. Create directory structure
    for root, dirs, files in os.walk(template_src):
        # Calculate relative path from template_src
        rel_path = os.path.relpath(root, template_src)
        if rel_path == '.':
            target_root = target_dir
        else:
            target_root = os.path.join(target_dir, rel_path)

        if any(ex in rel_path for ex in exclude):
            continue

        if not os.path.exists(target_root):
            os.makedirs(target_root)

        # 2. Copy and process files
        for file in files:
            if file in exclude:
                continue
            
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_root, file)

            # Skip binary files if any, but our templates are text
            try:
                with open(src_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace placeholders
                content = content.replace('{{PROJECT_NAME}}', project_name)
                content = content.replace('{{DATE}}', datetime.now(timezone.utc).strftime('%Y-%m-%d'))
                content = content.replace('{{TIMESTAMP}}', datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'))
                content = content.replace('{{SESSION_ID}}', 'INITIAL_BOOTSTRAP')
                content = content.replace('{{EXPORT_DESTINATION}}', 'TBD (Update in registry.json)')

                with open(dst_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  + Created: {os.path.relpath(dst_file, target_dir)}")
            except Exception as e:
                print(f"  ! Error processing {file}: {e}")

    print("\nInitialization Complete. Next steps:")
    print("1. Update meta_management/registry.json with target-specific constraints.")
    print("2. Define your architecture in meta_management/l3_semantic/MEMORY_ARCHITECTURE.md.")
    print("3. Start your first session by updating RESEARCH_STATE.md.")

if __name__ == "__main__":
    # If run directly: python setup_meta.py [target_path] [project_name]
    if len(sys.argv) < 3:
        print("Usage: python setup_meta.py <target_directory> <project_name>")
        sys.exit(1)

    target_path = os.path.abspath(sys.argv[1])
    p_name = sys.argv[2]
    
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    setup_meta(target_path, p_name)
