#!/usr/bin/env python3
"""
Script to organize the Ethical Hacking 2030 folder structure
"""

import os
import shutil
from pathlib import Path

def create_directory(path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def move_directory(src, dst):
    """Move directory from src to dst."""
    if os.path.exists(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")

def move_file(src, dst):
    """Move file from src to dst."""
    if os.path.exists(src):
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")

def remove_directory(path):
    """Remove directory if it exists."""
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Removed directory: {path}")
    except PermissionError:
        print(f"Could not remove directory: {path} (Permission denied)")

def main():
    """Main function to organize folders."""
    # Base directory
    base_dir = Path("Ethical_Hacking_2030")
    
    # Create main directories
    directories = [
        "modules",
        "tools",
        "evidence",
        "docs",
        "framework",
        "curriculum",
        "tests",
        "data",
        "config",
        "templates",
        "static"
    ]
    
    for directory in directories:
        create_directory(base_dir / directory)
    
    # Move directories
    moves = [
        ("tools", base_dir / "tools"),
        ("evidence", base_dir / "evidence"),
        ("docs", base_dir / "docs"),
        ("security_framework", base_dir / "framework"),
        ("modules", base_dir / "modules"),
        ("curriculum", base_dir / "curriculum")
    ]
    
    for src, dst in moves:
        move_directory(src, dst)
    
    # Move files
    file_moves = [
        ("README.md", base_dir / "README.md"),
        ("project_structure.md", base_dir / "docs" / "project_structure.md")
    ]
    
    for src, dst in file_moves:
        move_file(src, dst)
    
    # Remove unnecessary directories
    remove_dirs = [
        "Ethical_Hacking_2025",
        "temp_backup",
        "ethical_hacking",
        "learning_week",
        "personal_website"
    ]
    
    for directory in remove_dirs:
        remove_directory(directory)

if __name__ == "__main__":
    main() 