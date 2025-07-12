#!/usr/bin/env python3
"""
Generate Tree JSON for All Topics
Tạo tree.json cho tất cả 20 chủ đề chính
"""

import os
import json
from pathlib import Path

def build_tree(root_path, rel_path=""):
    """Xây dựng cây thư mục"""
    tree = []
    try:
        for entry in sorted(os.listdir(root_path)):
            full_path = os.path.join(root_path, entry)
            rel_entry_path = os.path.join(rel_path, entry)
            
            # Bỏ qua file tree.json nếu đã tồn tại
            if entry == 'tree.json':
                continue
                
            if os.path.isdir(full_path):
                tree.append({
                    "type": "folder",
                    "name": entry,
                    "path": rel_entry_path.replace("\\", "/"),
                    "children": build_tree(full_path, rel_entry_path)
                })
            else:
                # Chỉ thêm file markdown và txt
                if entry.endswith(('.md', '.txt', '.py', '.ipynb')):
                    tree.append({
                        "type": "file",
                        "name": entry,
                        "path": rel_entry_path.replace("\\", "/")
                    })
    except PermissionError:
        print(f"  ⚠️ Không thể truy cập: {root_path}")
    except Exception as e:
        print(f"  ❌ Lỗi khi quét: {root_path} - {e}")
    
    return tree

def generate_tree_for_topic(topic_folder):
    """Tạo tree.json cho một chủ đề"""
    if not os.path.exists(topic_folder):
        print(f"  ❌ Thư mục không tồn tại: {topic_folder}")
        return False
    
    try:
        tree = build_tree(topic_folder)
        out_path = Path(topic_folder) / "tree.json"
        
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(tree, f, ensure_ascii=False, indent=2)
        
        file_count = count_files(tree)
        print(f"  ✅ Tạo: {out_path.name} ({file_count} files)")
        return True
    except Exception as e:
        print(f"  ❌ Lỗi: {e}")
        return False

def count_files(tree):
    """Đếm số file trong tree"""
    count = 0
    for node in tree:
        if node['type'] == 'file':
            count += 1
        elif node['type'] == 'folder':
            count += count_files(node['children'])
    return count

def update_dashboard_with_tree(topic_name, topic_folder):
    """Cập nhật dashboard con để có tree view"""
    dashboard_file = f"21_Dashboard_Web/topic_dashboards/{topic_folder.lower().replace('_', '-')}.html"
    
    if not os.path.exists(dashboard_file):
        print(f"  ⚠️ Dashboard không tồn tại: {dashboard_file}")
        return False
    
    try:
        # Đọc nội dung hiện tại
        with open(dashboard_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra xem đã có tree view chưa
        if 'tree-view' in content and 'fetch(' in content:
            print(f"  ✅ Dashboard đã có tree view")
            return True
        
        # Tạo nội dung mới với tree view
        new_content = create_dashboard_with_tree(topic_name, topic_folder)
        
        # Ghi lại file
        with open(dashboard_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Cập nhật dashboard với tree view")
        return True
    except Exception as e:
        print(f"  ❌ Lỗi cập nhật dashboard: {e}")
        return False

def create_dashboard_with_tree(topic_name, topic_folder):
    """Tạo nội dung dashboard với tree view"""
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic_name} - AI/ML Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f7f7f7;
            color: #222;
            margin: 0;
            min-height: 100vh;
        }}
        .main-layout {{
            display: flex;
            min-height: 100vh;
        }}
        .sidebar {{
            width: 250px;
            background: #fff;
            border-right: 1px solid #e0e0e0;
            padding: 18px 10px 18px 18px;
            box-sizing: border-box;
            overflow-y: auto;
        }}
        .sidebar h2 {{
            font-size: 1.2rem;
            color: #2d5e8c;
            margin-bottom: 18px;
        }}
        .tree-view {{
            font-size: 1rem;
            line-height: 1.7;
        }}
        .tree-folder {{
            font-weight: 600;
            color: #2d5e8c;
            cursor: pointer;
            margin: 2px 0;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        .tree-folder:hover {{
            background: #f0f0f0;
        }}
        .tree-folder.collapsed > ul {{
            display: none;
        }}
        .tree-file {{
            color: #222;
            margin-left: 18px;
            cursor: pointer;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        .tree-file:hover {{
            background: #f0f0f0;
        }}
        .tree-file.selected {{
            background: #e0e0e0;
            border-radius: 5px;
        }}
        .content-area {{
            flex: 1;
            padding: 32px;
            background: #f7f7f7;
            min-height: 100vh;
            overflow-y: auto;
        }}
        .content-area h1 {{
            color: #2d5e8c;
            font-size: 1.5rem;
            margin-bottom: 12px;
        }}
        .content-area h2 {{
            color: #2d5e8c;
            font-size: 1.3rem;
            margin: 20px 0 10px 0;
        }}
        .content-area h3 {{
            color: #2d5e8c;
            font-size: 1.1rem;
            margin: 15px 0 8px 0;
        }}
        .content-area pre {{
            background: #f3f3f3;
            color: #222;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 10px 0;
        }}
        .content-area code {{
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #2d5e8c;
        }}
        .loading {{
            color: #888;
            padding: 20px;
        }}
        .error {{
            color: #c33;
            background: #fee;
            padding: 10px;
            border-radius: 6px;
            margin: 10px 0;
        }}
        .back-btn {{
            display: inline-block;
            margin: 18px;
            background: #e0e0e0;
            color: #222;
            border: none;
            padding: 7px 18px;
            border-radius: 20px;
            cursor: pointer;
            text-decoration: none;
            font-size: 1rem;
            transition: background 0.2s;
        }}
        .back-btn:hover {{
            background: #d0d0d0;
        }}
        @media (max-width: 900px) {{
            .main-layout {{ flex-direction: column; }}
            .sidebar {{ width: 100%; border-right: none; border-bottom: 1px solid #e0e0e0; }}
            .content-area {{ padding: 18px; }}
        }}
    </style>
</head>
<body>
    <a href="../index.html" class="back-btn">← Quay lại Dashboard chính</a>
    <div class="main-layout">
        <aside class="sidebar">
            <h2>📁 {topic_name}</h2>
            <div id="tree-view" class="tree-view">
                <div class="loading">Đang tải cấu trúc thư mục...</div>
            </div>
        </aside>
        <section class="content-area" id="content-area">
            <h1>Chọn file để xem nội dung</h1>
            <p>Bạn có thể duyệt toàn bộ thư mục và file của chủ đề {topic_name} ở sidebar bên trái.</p>
            <p>Click vào bất kỳ file nào để xem nội dung trực tiếp.</p>
        </section>
    </div>
    <script>
        // Load tree.json
        let selectedFile = null;
        
        fetch('../../{topic_folder}/tree.json')
            .then(res => {{
                if (!res.ok) {{
                    throw new Error('Không thể tải file tree.json');
                }}
                return res.json();
            }})
            .then(tree => {{
                renderTreeView(tree, document.getElementById('tree-view'));
            }})
            .catch(err => {{
                document.getElementById('tree-view').innerHTML = 
                    `<div class="error">Lỗi: ${{err.message}}<br>Hãy đảm bảo file tree.json đã được tạo.</div>`;
            }});

        function renderTreeView(tree, container) {{
            container.innerHTML = '';
            const ul = document.createElement('ul');
            ul.style.listStyle = 'none';
            ul.style.paddingLeft = '0';
            tree.forEach(node => {{
                ul.appendChild(renderNode(node));
            }});
            container.appendChild(ul);
        }}

        function renderNode(node) {{
            const li = document.createElement('li');
            if (node.type === 'folder') {{
                li.className = 'tree-folder';
                li.textContent = '📂 ' + node.name;
                li.onclick = function(e) {{
                    e.stopPropagation();
                    li.classList.toggle('collapsed');
                }};
                const childrenUl = document.createElement('ul');
                childrenUl.style.listStyle = 'none';
                childrenUl.style.paddingLeft = '18px';
                node.children.forEach(child => {{
                    childrenUl.appendChild(renderNode(child));
                }});
                li.appendChild(childrenUl);
            }} else {{
                li.className = 'tree-file';
                li.textContent = '📄 ' + node.name;
                li.onclick = function(e) {{
                    e.stopPropagation();
                    document.querySelectorAll('.tree-file').forEach(f => f.classList.remove('selected'));
                    li.classList.add('selected');
                    loadFileContent(node.path, node.name);
                }};
            }}
            return li;
        }}

        async function loadFileContent(filePath, fileName) {{
            const contentArea = document.getElementById('content-area');
            contentArea.innerHTML = `<div class="loading">Đang tải nội dung <b>${{fileName}}</b>...</div>`;
            
            try {{
                const res = await fetch('../../' + filePath);
                if (!res.ok) {{
                    throw new Error(`HTTP ${{res.status}}: Không thể tải file ${{filePath}}`);
                }}
                const text = await res.text();
                contentArea.innerHTML = `<h1>${{fileName}}</h1>` + markdownToHtml(text);
            }} catch (err) {{
                contentArea.innerHTML = `
                    <div class="error">
                        <strong>Lỗi khi tải file:</strong> ${{err.message}}
                        <br><br>
                        <strong>Đường dẫn:</strong> ${{filePath}}
                        <br><br>
                        <button onclick="window.open('../../${{filePath}}', '_blank')" 
                                style="background: #2d5e8c; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer;">
                            Mở file trực tiếp
                        </button>
                    </div>
                `;
            }}
        }}

        // Chuyển đổi markdown sang HTML
        function markdownToHtml(md) {{
            let html = md;
            
            // Headers
            html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
            html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
            html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
            
            // Bold and italic
            html = html.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
            html = html.replace(/\\*(.*?)\\*/g, '<em>$1</em>');
            
            // Code blocks
            html = html.replace(/```([\\s\\S]*?)```/g, '<pre><code>$1</code></pre>');
            html = html.replace(/`(.*?)`/g, '<code>$1</code>');
            
            // Lists
            html = html.replace(/^\\* (.*$)/gim, '<li>$1</li>');
            html = html.replace(/^- (.*$)/gim, '<li>$1</li>');
            html = html.replace(/^\\d+\\. (.*$)/gim, '<li>$1</li>');
            
            // Wrap lists
            html = html.replace(/(<li>.*<\\/li>)/s, '<ul>$1</ul>');
            
            // Links
            html = html.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2" target="_blank">$1</a>');
            
            // Paragraphs
            html = html.replace(/\\n\\n/g, '</p><p>');
            html = '<p>' + html + '</p>';
            
            return html;
        }}
    </script>
</body>
</html>"""

def main():
    """Hàm chính"""
    print("🚀 Bắt đầu tạo tree.json cho tất cả chủ đề...")
    print("=" * 60)
    
    # Danh sách các chủ đề chính
    topics = [
        ("01_Machine_Learning", "Machine Learning"),
        ("02_Deep_Learning", "Deep Learning"),
        ("03_Neural_Networks", "Neural Networks"),
        ("04_Natural_Language_Processing", "Natural Language Processing"),
        ("05_Computer_Vision", "Computer Vision"),
        ("06_Reinforcement_Learning", "Reinforcement Learning"),
        ("07_Generative_Models", "Generative Models"),
        ("08_Large_Language_Models", "Large Language Models"),
        ("09_Transformers", "Transformers"),
        ("10_Feature_Engineering", "Feature Engineering"),
        ("11_Supervised_Learning", "Supervised Learning"),
        ("12_Bayesian_Learning", "Bayesian Learning"),
        ("13_Prompt_Engineering", "Prompt Engineering"),
        ("14_AI_Agents", "AI Agents"),
        ("15_Fine_tuning_Models", "Fine-tuning Models"),
        ("16_Multimodal_Models", "Multimodal Models"),
        ("17_Embeddings", "Embeddings"),
        ("18_Vector_Search", "Vector Search"),
        ("19_Model_Evaluation", "Model Evaluation"),
        ("20_AI_Infrastructure", "AI Infrastructure")
    ]
    
    success_count = 0
    dashboard_count = 0
    
    for folder_name, topic_name in topics:
        print(f"🔧 Xử lý: {topic_name}")
        
        # Tạo tree.json
        if generate_tree_for_topic(folder_name):
            success_count += 1
        
        # Cập nhật dashboard
        if update_dashboard_with_tree(topic_name, folder_name):
            dashboard_count += 1
    
    print("\n" + "=" * 60)
    print(f"🎉 Hoàn thành!")
    print(f"✅ Đã tạo {success_count}/20 tree.json")
    print(f"✅ Đã cập nhật {dashboard_count}/20 dashboard")
    
    print("\n🌐 Cách sử dụng:")
    print("1. Mở trình duyệt và truy cập: http://localhost:8000")
    print("2. Vào topic_dashboards/ để xem các dashboard con")
    print("3. Mỗi dashboard có tree view bên trái để duyệt file")
    print("4. Click vào file để xem nội dung trực tiếp")

if __name__ == "__main__":
    main() 