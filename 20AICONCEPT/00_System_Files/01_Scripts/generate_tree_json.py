import os
import json
from pathlib import Path

def build_tree(root_path, rel_path=""):
    tree = []
    for entry in sorted(os.listdir(root_path)):
        full_path = os.path.join(root_path, entry)
        rel_entry_path = os.path.join(rel_path, entry)
        if os.path.isdir(full_path):
            tree.append({
                "type": "folder",
                "name": entry,
                "path": rel_entry_path.replace("\\", "/"),
                "children": build_tree(full_path, rel_entry_path)
            })
        else:
            tree.append({
                "type": "file",
                "name": entry,
                "path": rel_entry_path.replace("\\", "/")
            })
    return tree

def main():
    # Đổi đường dẫn này để quét chủ đề khác
    topic_folder = "01_Machine_Learning"
    tree = build_tree(topic_folder)
    out_path = Path(topic_folder) / "tree.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)
    print(f"Đã tạo {out_path} cho tree view!")

if __name__ == "__main__":
    main() 