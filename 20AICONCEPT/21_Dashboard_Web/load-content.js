// Hàm load nội dung từ file markdown
async function loadMarkdownContent(filePath) {
    try {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const content = await response.text();
        return content;
    } catch (error) {
        console.error('Error loading file:', error);
        return `<p>Không thể load file: ${filePath}</p><p>Lỗi: ${error.message}</p>`;
    }
}

// Hàm chuyển đổi markdown đơn giản thành HTML
function markdownToHtml(markdown) {
    let html = markdown;
    
    // Headers
    html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
    
    // Bold
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Italic
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    
    // Code blocks
    html = html.replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
    
    // Inline code
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');
    
    // Lists
    html = html.replace(/^\* (.*$)/gim, '<li>$1</li>');
    html = html.replace(/^- (.*$)/gim, '<li>$1</li>');
    html = html.replace(/^\d+\. (.*$)/gim, '<li>$1</li>');
    
    // Wrap lists
    html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');
    
    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
    
    // Paragraphs
    html = html.replace(/\n\n/g, '</p><p>');
    html = '<p>' + html + '</p>';
    
    return html;
}

// Hàm load và hiển thị nội dung từ file thực tế
async function loadRealContent(type, topic = '') {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = '<p>Đang tải nội dung...</p>';
    
    let filePath = '';
    let title = '';
    
    switch(type) {
        case 'theory':
            filePath = `../01_Machine_Learning/01_Algorithms/01_Linear_Regression/THEORY_01_linear_regression.md`;
            title = 'Lý Thuyết Linear Regression';
            break;
        case 'quiz':
            filePath = `../01_Machine_Learning/01_Algorithms/01_Linear_Regression/QUIZ_01_linear_regression.md`;
            title = 'Quiz Linear Regression';
            break;
        case 'problems':
            filePath = `../01_Machine_Learning/01_Algorithms/01_Linear_Regression/COMPLEX_PROBLEMS.md`;
            title = 'Bài Toán Phức Tạp - Linear Regression';
            break;
        case 'code':
            filePath = `../01_Machine_Learning/01_Algorithms/01_Linear_Regression/CODE_EXAMPLES_01_linear_regression.md`;
            title = 'Code Examples - Linear Regression';
            break;
        case 'project':
            filePath = `../01_Machine_Learning/01_Algorithms/01_Linear_Regression/PROJECT_01_linear_regression.md`;
            title = 'Project - Linear Regression';
            break;
        default:
            contentArea.innerHTML = '<p>Chọn loại nội dung để xem</p>';
            return;
    }
    
    try {
        const markdownContent = await loadMarkdownContent(filePath);
        const htmlContent = markdownToHtml(markdownContent);
        contentArea.innerHTML = `<h1>${title}</h1>${htmlContent}`;
    } catch (error) {
        contentArea.innerHTML = `<p>Lỗi khi tải nội dung: ${error.message}</p>`;
    }
}

// Hàm tạo danh sách các file có sẵn
function showAvailableFiles() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h2>📁 Các File Có Sẵn</h2>
        <div class="file-list">
            <div class="file-category">
                <h3>📖 Lý Thuyết</h3>
                <button onclick="loadRealContent('theory')">Linear Regression Theory</button>
            </div>
            <div class="file-category">
                <h3>🧠 Quiz</h3>
                <button onclick="loadRealContent('quiz')">Linear Regression Quiz</button>
            </div>
            <div class="file-category">
                <h3>❓ Bài Toán</h3>
                <button onclick="loadRealContent('problems')">Complex Problems</button>
            </div>
            <div class="file-category">
                <h3>💻 Code</h3>
                <button onclick="loadRealContent('code')">Code Examples</button>
            </div>
            <div class="file-category">
                <h3>🚀 Project</h3>
                <button onclick="loadRealContent('project')">Project</button>
            </div>
        </div>
    `;
} 