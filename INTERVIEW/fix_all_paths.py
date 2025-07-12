#!/usr/bin/env python3
"""
Comprehensive script to fix all CSS and JS file paths in HTML files
"""

import os
import re
from pathlib import Path

def fix_file_paths(file_path):
    """Fix CSS and JS file paths in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Get the directory level of the HTML file
        file_dir = Path(file_path).parent
        ui_dir = Path("AlgorithmEcosystem/ui")
        shared_dir = ui_dir / "shared"
        
        # Calculate relative path to shared directory
        try:
            relative_path = os.path.relpath(shared_dir, file_dir)
        except ValueError:
            # If on different drives, use absolute path
            relative_path = "../../shared"
        
        # Fix CSS paths
        content = re.sub(r'href="[^"]*shared/styles\.css"', f'href="{relative_path}/styles.css"', content)
        content = re.sub(r'href="[^"]*shared/components\.css"', f'href="{relative_path}/components.css"', content)
        content = re.sub(r'href="[^"]*shared/animations\.css"', f'href="{relative_path}/animations.css"', content)
        content = re.sub(r'href="[^"]*shared/accessibility\.css"', f'href="{relative_path}/accessibility.css"', content)
        content = re.sub(r'href="[^"]*shared/utilities\.css"', f'href="{relative_path}/utilities.css"', content)
        
        # Fix JS paths
        content = re.sub(r'src="[^"]*shared/scripts\.js"', f'src="{relative_path}/scripts.js"', content)
        
        # Fix preload paths
        content = re.sub(r'href="[^"]*shared/styles\.css" as="style"', f'href="{relative_path}/styles.css" as="style"', content)
        content = re.sub(r'href="[^"]*shared/scripts\.js" as="script"', f'href="{relative_path}/scripts.js" as="script"', content)
        
        # Fix icon and manifest paths
        if "ui/" in str(file_path):
            content = re.sub(r'href="icons/([^"]+)"', r'href="../icons/\1"', content)
            content = re.sub(r'href="manifest\.json"', r'href="../manifest.json"', content)
            content = re.sub(r'href="sw\.js"', r'href="../sw.js"', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {file_path}")
            return True
        else:
            print(f"⏭️  No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all HTML files"""
    print("🔧 Fixing all CSS and JS file paths in HTML files...")
    
    # Find all HTML files in AlgorithmEcosystem
    base_dir = Path("AlgorithmEcosystem")
    html_files = list(base_dir.rglob("*.html"))
    
    total_files = 0
    fixed_files = 0
    
    for file_path in html_files:
        total_files += 1
        if fix_file_paths(str(file_path)):
            fixed_files += 1
    
    print(f"\n🎉 Summary:")
    print(f"   Total HTML files processed: {total_files}")
    print(f"   Files fixed: {fixed_files}")
    print(f"   Files unchanged: {total_files - fixed_files}")

if __name__ == "__main__":
    main() 