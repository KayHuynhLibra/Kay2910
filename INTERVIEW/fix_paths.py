#!/usr/bin/env python3
"""
Script to fix CSS and JS file paths in all HTML files
"""

import os
import re
from pathlib import Path

def fix_file_paths(file_path):
    """Fix CSS and JS file paths in a single HTML file"""
    try:
        print(f"Processing: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix CSS paths - remove incorrect ../ prefix
        content = re.sub(r'href="\.\./shared/([^"]+)"', r'href="shared/\1"', content)
        content = re.sub(r'href="\.\./\.\./shared/([^"]+)"', r'href="../../shared/\1"', content)
        
        # Fix JS paths
        content = re.sub(r'src="\.\./shared/([^"]+)"', r'src="shared/\1"', content)
        content = re.sub(r'src="\.\./\.\./shared/([^"]+)"', r'src="../../shared/\1"', content)
        
        # Fix preload paths
        content = re.sub(r'href="\.\./shared/([^"]+)" as="style"', r'href="shared/\1" as="style"', content)
        content = re.sub(r'href="\.\./\.\./shared/([^"]+)" as="style"', r'href="../../shared/\1" as="style"', content)
        content = re.sub(r'href="\.\./shared/([^"]+)" as="script"', r'href="shared/\1" as="script"', content)
        content = re.sub(r'href="\.\./\.\./shared/([^"]+)" as="script"', r'href="../../shared/\1" as="script"', content)
        
        # Fix icon and manifest paths
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
    print("🔧 Fixing CSS and JS file paths in HTML files...")
    
    # Define directories to search
    directories = [
        "AlgorithmEcosystem/ui",
        "AlgorithmEcosystem/ui/analyzers", 
        "AlgorithmEcosystem/ui/learning",
        "AlgorithmEcosystem/ui/dashboards",
        "AlgorithmEcosystem/ui/viewers",
        "AlgorithmEcosystem/ui/components"
    ]
    
    total_files = 0
    fixed_files = 0
    
    for directory in directories:
        print(f"\n📁 Checking directory: {directory}")
        if os.path.exists(directory):
            print(f"✅ Directory exists: {directory}")
            html_files = list(Path(directory).rglob("*.html"))
            print(f"Found {len(html_files)} HTML files")
            for file_path in html_files:
                total_files += 1
                if fix_file_paths(str(file_path)):
                    fixed_files += 1
        else:
            print(f"⚠️  Directory not found: {directory}")
    
    print(f"\n🎉 Summary:")
    print(f"   Total HTML files processed: {total_files}")
    print(f"   Files fixed: {fixed_files}")
    print(f"   Files unchanged: {total_files - fixed_files}")

if __name__ == "__main__":
    main() 