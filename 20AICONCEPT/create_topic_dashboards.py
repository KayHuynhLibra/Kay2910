#!/usr/bin/env python3
"""
Create Topic Dashboards Script
Tạo dashboard con cho từng chủ đề chính với giao diện chi tiết
"""

import os
from pathlib import Path
import json

def create_topic_dashboard_html(topic_name, topic_folder):
    """Tạo file HTML dashboard cho từng chủ đề"""
    
    # Lấy danh sách các file có sẵn trong thư mục
    files = []
    if topic_folder.exists():
        for file in topic_folder.glob("*.md"):
            if file.is_file():
                file_type = get_file_type(file.name)
                # Sửa lỗi lấy đường dẫn tương đối
                try:
                    rel_path = file.relative_to(Path("21_Dashboard_Web/topic_dashboards").parent)
                except ValueError:
                    rel_path = os.path.relpath(file, Path("21_Dashboard_Web/topic_dashboards").parent)
                files.append({
                    'name': file.name,
                    'type': file_type,
                    'path': str(rel_path).replace('\\', '/'),
                    'icon': get_file_icon(file_type)
                })
    
    html_content = f"""<!DOCTYPE html>
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
            line-height: 1.6;
            min-height: 100vh;
        }}
        .dashboard-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 24px 8px 32px 8px;
        }}
        .header {{
            background: #fff;
            padding: 16px 20px;
            border-radius: 8px;
            margin-bottom: 18px;
            border: 1px solid #e0e0e0;
            text-align: center;
        }}
        .header h1 {{
            color: #2d5e8c;
            font-size: 2rem;
            margin-bottom: 6px;
        }}
        .header p {{
            color: #555;
            font-size: 1rem;
        }}
        .back-btn {{
            display: inline-block;
            margin-bottom: 18px;
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
        .stats-grid {{
            display: flex;
            gap: 16px;
            margin-bottom: 18px;
            flex-wrap: wrap;
        }}
        .stat-card {{
            background: #fff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 12px 18px;
            text-align: center;
            flex: 1 1 120px;
            min-width: 120px;
        }}
        .stat-number {{
            font-size: 1.3rem;
            font-weight: bold;
            color: #2d5e8c;
            margin-bottom: 2px;
        }}
        .stat-label {{
            color: #666;
            font-size: 0.95rem;
        }}
        .quick-actions {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }}
        .action-btn {{
            background: #e0e0e0;
            color: #222;
            border: none;
            padding: 8px 18px;
            border-radius: 18px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.2s;
        }}
        .action-btn:hover {{
            background: #d0d0d0;
        }}
        .content-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            margin-bottom: 18px;
        }}
        .content-section {{
            background: #fff;
            border: 1px solid #e0e0e0;
            padding: 14px 12px;
            border-radius: 8px;
        }}
        .section-header {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
            border-bottom: 1px solid #f0f0f0;
            padding-bottom: 6px;
        }}
        .section-icon {{
            font-size: 1.2rem;
            margin-right: 8px;
        }}
        .section-title {{
            font-size: 1.1rem;
            color: #2d5e8c;
            font-weight: 600;
        }}
        .file-list {{
            list-style: none;
            padding-left: 0;
        }}
        .file-item {{
            display: flex;
            align-items: center;
            padding: 7px 0;
            margin-bottom: 2px;
            border-bottom: 1px solid #f3f3f3;
            cursor: pointer;
            font-size: 1rem;
        }}
        .file-item:last-child {{
            border-bottom: none;
        }}
        .file-icon {{
            font-size: 1rem;
            margin-right: 8px;
            width: 18px;
            text-align: center;
        }}
        .file-name {{
            flex: 1;
            font-weight: 500;
        }}
        .file-type {{
            background: #f0f0f0;
            color: #2d5e8c;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 0.8rem;
            font-weight: 500;
        }}
        .content-viewer {{
            background: #fff;
            border: 1px solid #e0e0e0;
            padding: 18px 16px;
            border-radius: 8px;
            min-height: 200px;
            display: none;
        }}
        .content-viewer.active {{
            display: block;
        }}
        .content-viewer h2 {{
            color: #2d5e8c;
            margin-bottom: 12px;
            font-size: 1.2rem;
        }}
        .content-viewer pre {{
            background: #f3f3f3;
            color: #222;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 10px 0;
        }}
        .content-viewer code {{
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #2d5e8c;
        }}
        .loading {{
            text-align: center;
            padding: 20px;
            color: #666;
        }}
        .error {{
            background: #fee;
            color: #c33;
            padding: 10px;
            border-radius: 6px;
            margin: 10px 0;
        }}
        @media (max-width: 768px) {{
            .dashboard-container {{
                padding: 6px;
            }}
            .content-grid {{
                grid-template-columns: 1fr;
            }}
            .stats-grid {{
                flex-direction: column;
            }}
        }}
        .dark-theme {{
            background: #23272b;
            color: #e2e8f0;
        }}
        .dark-theme .header,
        .dark-theme .content-section,
        .dark-theme .stat-card,
        .dark-theme .content-viewer {{
            background: #2d3135;
            color: #e2e8f0;
            border-color: #444;
        }}
        .dark-theme .file-item {{
            background: none;
            color: #e2e8f0;
        }}
        .dark-theme .file-type {{
            background: #444;
            color: #a3d0f7;
        }}
    </style>
</head>
<body>
    <div class="dashboard-container">
        <a href="../index.html" class="back-btn">← Quay lại Dashboard chính</a>
        
        <div class="header">
            <h1>🎯 {topic_name}</h1>
            <p>Khám phá chi tiết về {topic_name} với các tài liệu lý thuyết, code examples, và bài tập thực hành</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{len(files)}</div>
                <div class="stat-label">Tài liệu có sẵn</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len([f for f in files if 'theory' in f['name'].lower()])}</div>
                <div class="stat-label">Lý thuyết</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len([f for f in files if 'code' in f['name'].lower()])}</div>
                <div class="stat-label">Code Examples</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len([f for f in files if 'problem' in f['name'].lower()])}</div>
                <div class="stat-label">Bài toán</div>
            </div>
        </div>

        <div class="quick-actions">
            <button class="action-btn" onclick="showAllFiles()">📁 Xem tất cả tài liệu</button>
            <button class="action-btn" onclick="showTheory()">📖 Lý thuyết</button>
            <button class="action-btn" onclick="showCode()">💻 Code Examples</button>
            <button class="action-btn" onclick="showProblems()">❓ Bài toán</button>
            <button class="action-btn" onclick="toggleTheme()">🌙 Dark Mode</button>
        </div>

        <div class="content-grid">
            <div class="content-section">
                <div class="section-header">
                    <span class="section-icon">📖</span>
                    <h3 class="section-title">Lý Thuyết</h3>
                </div>
                <ul class="file-list" id="theory-files">
                    {generate_file_list(files, 'theory')}
                </ul>
            </div>

            <div class="content-section">
                <div class="section-header">
                    <span class="section-icon">💻</span>
                    <h3 class="section-title">Code Examples</h3>
                </div>
                <ul class="file-list" id="code-files">
                    {generate_file_list(files, 'code')}
                </ul>
            </div>

            <div class="content-section">
                <div class="section-header">
                    <span class="section-icon">❓</span>
                    <h3 class="section-title">Bài Toán & Quiz</h3>
                </div>
                <ul class="file-list" id="problem-files">
                    {generate_file_list(files, 'problem')}
                </ul>
            </div>

            <div class="content-section">
                <div class="section-header">
                    <span class="section-icon">🚀</span>
                    <h3 class="section-title">Projects & Implementation</h3>
                </div>
                <ul class="file-list" id="project-files">
                    {generate_file_list(files, 'project')}
                </ul>
            </div>

            <div class="content-section">
                <div class="section-header">
                    <span class="section-icon">✅</span>
                    <h3 class="section-title">Validation & Analysis</h3>
                </div>
                <ul class="file-list" id="validation-files">
                    {generate_file_list(files, 'validation')}
                </ul>
            </div>

            <div class="content-section">
                <div class="section-header">
                    <span class="section-icon">🔬</span>
                    <h3 class="section-title">Research & Math</h3>
                </div>
                <ul class="file-list" id="research-files">
                    {generate_file_list(files, 'research')}
                </ul>
            </div>
        </div>

        <div class="content-viewer" id="content-viewer">
            <h2 id="viewer-title">Nội dung sẽ hiển thị ở đây</h2>
            <div id="viewer-content">
                <p>Chọn một file để xem nội dung chi tiết.</p>
            </div>
        </div>
    </div>

    <script>
        const files = {json.dumps(files)};
        let currentTheme = 'light';

        function showAllFiles() {{
            const viewer = document.getElementById('content-viewer');
            const title = document.getElementById('viewer-title');
            const content = document.getElementById('viewer-content');
            
            title.textContent = '📁 Tất cả tài liệu có sẵn';
            content.innerHTML = `
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
                    ${{files.map(file => `
                        <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; cursor: pointer;" onclick="loadFile('${{file.path}}', '${{file.name}}')">
                            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                <span style="font-size: 1.5rem; margin-right: 10px;">${{file.icon}}</span>
                                <span style="font-weight: 500;">${{file.name}}</span>
                            </div>
                            <span style="background: #667eea; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;">${{file.type}}</span>
                        </div>
                    `).join('')}}
                </div>
            `;
            viewer.classList.add('active');
        }}

        function showTheory() {{
            const theoryFiles = files.filter(f => f.type === 'Theory');
            displayFileCategory(theoryFiles, '📖 Lý Thuyết');
        }}

        function showCode() {{
            const codeFiles = files.filter(f => f.type === 'Code');
            displayFileCategory(codeFiles, '💻 Code Examples');
        }}

        function showProblems() {{
            const problemFiles = files.filter(f => f.type === 'Problem' || f.type === 'Quiz');
            displayFileCategory(problemFiles, '❓ Bài Toán & Quiz');
        }}

        function displayFileCategory(fileList, title) {{
            const viewer = document.getElementById('content-viewer');
            const titleEl = document.getElementById('viewer-title');
            const content = document.getElementById('viewer-content');
            
            titleEl.textContent = title;
            content.innerHTML = `
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
                    ${{fileList.map(file => `
                        <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; cursor: pointer;" onclick="loadFile('${{file.path}}', '${{file.name}}')">
                            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                                <span style="font-size: 1.5rem; margin-right: 10px;">${{file.icon}}</span>
                                <span style="font-weight: 500;">${{file.name}}</span>
                            </div>
                            <span style="background: #667eea; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;">${{file.type}}</span>
                        </div>
                    `).join('')}}
                </div>
            `;
            viewer.classList.add('active');
        }}

        async function loadFile(filePath, fileName) {{
            const viewer = document.getElementById('content-viewer');
            const title = document.getElementById('viewer-title');
            const content = document.getElementById('viewer-content');
            
            title.textContent = `📄 ${{fileName}}`;
            content.innerHTML = '<div class="loading">Đang tải nội dung...</div>';
            viewer.classList.add('active');
            
            try {{
                const response = await fetch(filePath);
                if (!response.ok) {{
                    throw new Error(`HTTP error! status: ${{response.status}}`);
                }}
                const text = await response.text();
                
                // Convert markdown to HTML (simple conversion)
                const html = convertMarkdownToHtml(text);
                content.innerHTML = html;
                
            }} catch (error) {{
                content.innerHTML = `
                    <div class="error">
                        <strong>Lỗi khi tải file:</strong> ${{error.message}}
                        <br><br>
                        <strong>Đường dẫn:</strong> ${{filePath}}
                        <br><br>
                        <button onclick="window.open('${{filePath}}', '_blank')" style="background: #667eea; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer;">
                            Mở file trực tiếp
                        </button>
                    </div>
                `;
            }}
        }}

        function convertMarkdownToHtml(markdown) {{
            let html = markdown;
            
            // Headers
            html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
            html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
            html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
            
            // Bold and italic
            html = html.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
            html = html.replace(/\\*(.*?)\\*/g, '<em>$1</em>');
            
            // Code blocks
            html = html.replace(/```(\\w+)?\\n([\\s\\S]*?)```/g, '<pre><code>$2</code></pre>');
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

        function toggleTheme() {{
            const body = document.body;
            if (currentTheme === 'light') {{
                body.classList.add('dark-theme');
                currentTheme = 'dark';
            }} else {{
                body.classList.remove('dark-theme');
                currentTheme = 'light';
            }}
        }}

        // Add click handlers to all file items
        document.addEventListener('DOMContentLoaded', function() {{
            const fileItems = document.querySelectorAll('.file-item');
            fileItems.forEach(item => {{
                item.addEventListener('click', function() {{
                    const filePath = this.getAttribute('data-path');
                    const fileName = this.getAttribute('data-name');
                    if (filePath && fileName) {{
                        loadFile(filePath, fileName);
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>"""
    
    return html_content

def get_file_type(filename):
    """Xác định loại file dựa trên tên"""
    filename_lower = filename.lower()
    
    if 'theory' in filename_lower:
        return 'Theory'
    elif 'code' in filename_lower:
        return 'Code'
    elif 'problem' in filename_lower or 'complex' in filename_lower:
        return 'Problem'
    elif 'quiz' in filename_lower:
        return 'Quiz'
    elif 'project' in filename_lower:
        return 'Project'
    elif 'implementation' in filename_lower:
        return 'Implementation'
    elif 'best_practice' in filename_lower:
        return 'Best Practice'
    elif 'accuracy' in filename_lower:
        return 'Accuracy Analysis'
    elif 'mathematical' in filename_lower:
        return 'Mathematical Foundation'
    elif 'validation' in filename_lower:
        return 'Validation Framework'
    elif 'research' in filename_lower:
        return 'Research Methodology'
    else:
        return 'Other'

def get_file_icon(file_type):
    """Lấy icon cho loại file"""
    icons = {
        'Theory': '📖',
        'Code': '💻',
        'Problem': '❓',
        'Quiz': '🧠',
        'Project': '🚀',
        'Implementation': '⚙️',
        'Best Practice': '✅',
        'Accuracy Analysis': '📊',
        'Mathematical Foundation': '🧮',
        'Validation Framework': '🔍',
        'Research Methodology': '🔬',
        'Other': '📄'
    }
    return icons.get(file_type, '📄')

def generate_file_list(files, category):
    """Tạo danh sách file cho một category"""
    category_files = []
    
    if category == 'theory':
        category_files = [f for f in files if 'theory' in f['name'].lower()]
    elif category == 'code':
        category_files = [f for f in files if 'code' in f['name'].lower()]
    elif category == 'problem':
        category_files = [f for f in files if 'problem' in f['name'].lower() or 'quiz' in f['name'].lower()]
    elif category == 'project':
        category_files = [f for f in files if 'project' in f['name'].lower() or 'implementation' in f['name'].lower()]
    elif category == 'validation':
        category_files = [f for f in files if 'validation' in f['name'].lower() or 'accuracy' in f['name'].lower()]
    elif category == 'research':
        category_files = [f for f in files if 'research' in f['name'].lower() or 'mathematical' in f['name'].lower()]
    
    if not category_files:
        return '<li style="color: #999; font-style: italic;">Chưa có tài liệu</li>'
    
    html_list = []
    for file in category_files:
        html_list.append(f'''
            <li class="file-item" data-path="{file['path']}" data-name="{file['name']}">
                <span class="file-icon">{file['icon']}</span>
                <span class="file-name">{file['name']}</span>
                <span class="file-type">{file['type']}</span>
            </li>
        ''')
    
    return ''.join(html_list)

def create_topic_dashboards():
    """Tạo dashboard cho tất cả các chủ đề chính"""
    
    # Các thư mục chính
    main_folders = [
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
    
    created_dashboards = []
    
    # Tạo thư mục cho dashboards
    dashboard_dir = Path("21_Dashboard_Web/topic_dashboards")
    dashboard_dir.mkdir(exist_ok=True)
    
    for folder_name, topic_name in main_folders:
        folder_path = Path(folder_name)
        if folder_path.exists():
            print(f"🔧 Tạo dashboard cho: {topic_name}")
            
            try:
                # Tạo HTML dashboard
                html_content = create_topic_dashboard_html(topic_name, folder_path)
                
                # Lưu file HTML
                html_file = dashboard_dir / f"{folder_name.lower().replace('_', '-')}.html"
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                created_dashboards.append(html_file)
                print(f"  ✅ Tạo: {html_file.name}")
                
            except Exception as e:
                print(f"  ❌ Lỗi khi tạo dashboard cho {topic_name}: {e}")
    
    return created_dashboards

def update_main_dashboard():
    """Cập nhật dashboard chính để link đến các dashboard con"""
    
    main_dashboard_path = Path("21_Dashboard_Web/index.html")
    if not main_dashboard_path.exists():
        print("❌ Không tìm thấy dashboard chính")
        return
    
    # Đọc nội dung hiện tại
    with open(main_dashboard_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thêm link đến topic dashboards trong topics.html
    topics_path = Path("21_Dashboard_Web/topics.html")
    if topics_path.exists():
        with open(topics_path, 'r', encoding='utf-8') as f:
            topics_content = f.read()
        
        # Thêm nút "Xem Dashboard Chi Tiết" cho mỗi topic
        updated_topics = topics_content.replace(
            'Mở thư mục →',
            'Mở thư mục →<br><a href="topic_dashboards/01-machine-learning.html" class="action-btn" style="margin-top: 10px; display: inline-block;">🎯 Xem Dashboard Chi Tiết</a>'
        )
        
        with open(topics_path, 'w', encoding='utf-8') as f:
            f.write(updated_topics)
        
        print("✅ Đã cập nhật topics.html với link đến dashboards chi tiết")

if __name__ == "__main__":
    print("🚀 Bắt đầu tạo dashboards chi tiết cho từng chủ đề...")
    print("=" * 60)
    
    created_dashboards = create_topic_dashboards()
    update_main_dashboard()
    
    print("\n" + "=" * 60)
    print(f"🎉 Hoàn thành! Đã tạo {len(created_dashboards)} dashboard chi tiết")
    print("\n📋 Các dashboard đã tạo:")
    for dashboard in created_dashboards:
        print(f"  - {dashboard.name}")
    
    print("\n🎯 Cách sử dụng:")
    print("1. Mở dashboard chính: 21_Dashboard_Web/index.html")
    print("2. Click 'Chủ Đề' để xem 20 chủ đề")
    print("3. Click 'Xem Dashboard Chi Tiết' để vào dashboard con")
    print("4. Trong dashboard con, click vào file để xem nội dung")
    
    print("\n✨ Tính năng dashboard con:")
    print("   - Giao diện đẹp với gradient background")
    print("   - Phân loại file theo loại")
    print("   - Xem nội dung trực tiếp trong browser")
    print("   - Dark/Light theme toggle")
    print("   - Responsive design")
    print("   - Thống kê số lượng file")
    print("   - Quick actions") 