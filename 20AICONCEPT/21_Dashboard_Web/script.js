// Toggle sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

// Toggle theme
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    const themeBtn = document.querySelector('.theme-btn');
    if (document.body.classList.contains('dark-theme')) {
        themeBtn.textContent = '☀️';
    } else {
        themeBtn.textContent = '🌙';
    }
}

// Load content function
function loadContent(page) {
    const contentArea = document.getElementById('content-area');
    
    // Remove active class from all nav items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    // Add active class to clicked item
    event.target.closest('.nav-item').classList.add('active');
    
    // Load content based on page
    switch(page) {
        case 'overview':
            loadOverview();
            break;
        case 'topics':
            loadTopics();
            break;
        case 'browse':
            loadBrowse();
            break;
        case 'theory':
            loadTheory();
            break;
        case 'quiz':
            loadQuiz();
            break;
        case 'code':
            loadCode();
            break;
        case 'project':
            loadProject();
            break;
        case 'datasets':
            loadDatasets();
            break;
        case 'roadmap':
            loadRoadmap();
            break;
        case 'exercises':
            loadExercises();
            break;
        case 'resources':
            loadResources();
            break;
        default:
            loadOverview();
    }
}

// Load overview content
function loadOverview() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>🤖 Chào mừng đến với AI/ML Learning Dashboard</h1>
        <p>Đây là hệ thống học tập toàn diện về Trí tuệ nhân tạo và Machine Learning với 20 chủ đề chính.</p>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>📚 20 Chủ Đề Chính</h3>
                <p>Machine Learning, Deep Learning, Neural Networks, NLP, Computer Vision và nhiều hơn nữa</p>
            </div>
            <div class="stat-card">
                <h3>📁 869 Thư Mục Con</h3>
                <p>Mỗi chủ đề có nhiều thư mục con với nội dung chi tiết</p>
            </div>
            <div class="stat-card">
                <h3>📄 3,785+ Bài Toán</h3>
                <p>Bài toán phức tạp để thực hành và kiểm tra kiến thức</p>
            </div>
            <div class="stat-card">
                <h3>💻 Code Examples</h3>
                <p>Ví dụ code thực tế cho mọi chủ đề</p>
            </div>
        </div>
        
        <h2>🚀 Bắt Đầu Học Tập</h2>
        <p>Chọn một chủ đề từ menu bên trái hoặc sử dụng "Xem Nội Dung Thực" để xem các file đã tạo.</p>
        
        <div class="quick-actions">
            <button onclick="loadContent('topics')" class="action-btn">📚 Xem Tất Cả Chủ Đề</button>
            <button onclick="showAvailableFiles()" class="action-btn">📄 Xem Nội Dung Thực</button>
            <button onclick="loadContent('roadmap')" class="action-btn">🗺️ Lộ Trình Học Tập</button>
        </div>
    `;
}

// Load topics content
function loadTopics() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>📚 20 Chủ Đề AI/ML</h1>
        <p>Khám phá các chủ đề chính trong lĩnh vực AI/ML:</p>
        
        <div class="topics-grid">
            <div class="topic-card">
                <h3>01. Machine Learning</h3>
                <p>Thuật toán cơ bản, thống kê, huấn luyện mô hình</p>
                <a href="../01_Machine_Learning/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>02. Deep Learning</h3>
                <p>Neural networks, CNN, RNN, LSTM, Transformers</p>
                <a href="../02_Deep_Learning/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>03. Neural Networks</h3>
                <p>Kiến trúc, hàm kích hoạt, tối ưu hóa</p>
                <a href="../03_Neural_Networks/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>04. Natural Language Processing</h3>
                <p>Xử lý ngôn ngữ tự nhiên, mô hình ngôn ngữ</p>
                <a href="../04_Natural_Language_Processing/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>05. Computer Vision</h3>
                <p>Xử lý ảnh, phát hiện đối tượng, phân đoạn ảnh</p>
                <a href="../05_Computer_Vision/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>06. Reinforcement Learning</h3>
                <p>Học tăng cường, Q-learning, policy gradient</p>
                <a href="../06_Reinforcement_Learning/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>07. Generative Models</h3>
                <p>GANs, VAEs, Diffusion Models</p>
                <a href="../07_Generative_Models/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>08. Large Language Models</h3>
                <p>Kiến trúc, huấn luyện, fine-tuning</p>
                <a href="../08_Large_Language_Models/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>09. Transformers</h3>
                <p>Attention mechanism, kiến trúc transformer</p>
                <a href="../09_Transformers/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>10. Feature Engineering</h3>
                <p>Trích xuất, chọn lọc, biến đổi đặc trưng</p>
                <a href="../10_Feature_Engineering/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>11. Supervised Learning</h3>
                <p>Phân loại, hồi quy, ensemble methods</p>
                <a href="../11_Supervised_Learning/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>12. Bayesian Learning</h3>
                <p>Mạng Bayesian, MCMC, variational inference</p>
                <a href="../12_Bayesian_Learning/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>13. Prompt Engineering</h3>
                <p>Kỹ thuật viết prompt, few-shot learning</p>
                <a href="../13_Prompt_Engineering/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>14. AI Agents</h3>
                <p>Loại agent, kiến trúc, multi-agent systems</p>
                <a href="../14_AI_Agents/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>15. Fine-tuning Models</h3>
                <p>Transfer learning, parameter efficient tuning</p>
                <a href="../15_Fine_tuning_Models/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>16. Multimodal Models</h3>
                <p>Mô hình đa phương thức, fusion strategies</p>
                <a href="../16_Multimodal_Models/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>17. Embeddings</h3>
                <p>Word embeddings, sentence embeddings, graph embeddings</p>
                <a href="../17_Embeddings/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>18. Vector Search</h3>
                <p>Tìm kiếm vector, indexing, similarity metrics</p>
                <a href="../18_Vector_Search/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>19. Model Evaluation</h3>
                <p>Metrics, validation, testing</p>
                <a href="../19_Model_Evaluation/" target="_blank">Mở thư mục →</a>
            </div>
            <div class="topic-card">
                <h3>20. AI Infrastructure</h3>
                <p>Hạ tầng AI, deployment, scaling</p>
                <a href="../20_AI_Infrastructure/" target="_blank">Mở thư mục →</a>
            </div>
        </div>
    `;
}

// Load browse content
function loadBrowse() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>📁 Duyệt Files</h1>
        <p>Khám phá cấu trúc file và nội dung trong hệ thống:</p>
        
        <div class="browse-section">
            <h3>📊 Thống Kê Hệ Thống</h3>
            <ul>
                <li><strong>20 thư mục chính:</strong> Mỗi thư mục đại diện cho một chủ đề AI/ML</li>
                <li><strong>869 thư mục con:</strong> Chứa nội dung chi tiết cho từng chủ đề</li>
                <li><strong>3,785+ bài toán:</strong> Bài toán phức tạp để thực hành</li>
                <li><strong>Code examples:</strong> Ví dụ code thực tế cho mọi chủ đề</li>
                <li><strong>Lý thuyết:</strong> Tài liệu lý thuyết chi tiết</li>
            </ul>
        </div>
        
        <div class="browse-section">
            <h3>🔗 Quick Links</h3>
            <div class="quick-links">
                <a href="../README.md" target="_blank">📋 README chính</a>
                <a href="../00_System_Files/" target="_blank">⚙️ System Files</a>
                <a href="../01_Machine_Learning/" target="_blank">🤖 Machine Learning</a>
                <a href="../02_Deep_Learning/" target="_blank">🧠 Deep Learning</a>
                <a href="../03_Neural_Networks/" target="_blank">🕸️ Neural Networks</a>
                <a href="../04_Natural_Language_Processing/" target="_blank">💬 NLP</a>
                <a href="../05_Computer_Vision/" target="_blank">👁️ Computer Vision</a>
            </div>
        </div>
        
        <div class="browse-section">
            <h3>📄 Loại File</h3>
            <div class="file-types">
                <div class="file-type">
                    <h4>📖 THEORY_*.md</h4>
                    <p>Tài liệu lý thuyết chi tiết</p>
                </div>
                <div class="file-type">
                    <h4>💻 CODE_EXAMPLES_*.md</h4>
                    <p>Ví dụ code thực tế</p>
                </div>
                <div class="file-type">
                    <h4>❓ COMPLEX_PROBLEMS.md</h4>
                    <p>Bài toán phức tạp</p>
                </div>
                <div class="file-type">
                    <h4>🚀 PROJECT_*.md</h4>
                    <p>Dự án thực hành</p>
                </div>
                <div class="file-type">
                    <h4>🧠 QUIZ_*.md</h4>
                    <p>Quiz kiểm tra kiến thức</p>
                </div>
                <div class="file-type">
                    <h4>📋 requirements.txt</h4>
                    <p>Dependencies và thư viện</p>
                </div>
            </div>
        </div>
    `;
}

// Load other content functions
function loadTheory() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>📖 Lý Thuyết</h1>
        <p>Chọn chủ đề để xem lý thuyết chi tiết:</p>
        <button onclick="showAvailableFiles()" class="action-btn">📄 Xem Nội Dung Thực</button>
    `;
}

function loadQuiz() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>🧠 Quiz</h1>
        <p>Kiểm tra kiến thức với các câu hỏi quiz:</p>
        <button onclick="showAvailableFiles()" class="action-btn">📄 Xem Nội Dung Thực</button>
    `;
}

function loadCode() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>💻 Code Examples</h1>
        <p>Xem các ví dụ code thực tế:</p>
        <button onclick="showAvailableFiles()" class="action-btn">📄 Xem Nội Dung Thực</button>
    `;
}

function loadProject() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>🚀 Projects</h1>
        <p>Thực hành với các dự án thực tế:</p>
        <button onclick="showAvailableFiles()" class="action-btn">📄 Xem Nội Dung Thực</button>
    `;
}

function loadDatasets() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>📊 Datasets</h1>
        <p>Bộ dữ liệu để thực hành và nghiên cứu:</p>
        <ul>
            <li>MNIST - Nhận dạng chữ số viết tay</li>
            <li>CIFAR-10 - Phân loại ảnh</li>
            <li>IMDB - Phân tích sentiment</li>
            <li>Boston Housing - Hồi quy</li>
            <li>Iris - Phân loại hoa</li>
        </ul>
    `;
}

function loadRoadmap() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>🗺️ Lộ Trình Học Tập</h1>
        <p>Hướng dẫn học tập từ cơ bản đến nâng cao:</p>
        
        <div class="roadmap-section">
            <h3>🎯 Giai Đoạn 1: Nền Tảng (2-3 tháng)</h3>
            <ul>
                <li>Machine Learning cơ bản</li>
                <li>Thống kê và xác suất</li>
                <li>Python và thư viện ML</li>
                <li>Feature Engineering</li>
            </ul>
        </div>
        
        <div class="roadmap-section">
            <h3>🚀 Giai Đoạn 2: Deep Learning (3-4 tháng)</h3>
            <ul>
                <li>Neural Networks</li>
                <li>CNN cho Computer Vision</li>
                <li>RNN/LSTM cho NLP</li>
                <li>Transformers</li>
            </ul>
        </div>
        
        <div class="roadmap-section">
            <h3>⚡ Giai Đoạn 3: Nâng Cao (2-3 tháng)</h3>
            <ul>
                <li>Reinforcement Learning</li>
                <li>Generative Models</li>
                <li>Large Language Models</li>
                <li>AI Infrastructure</li>
            </ul>
        </div>
    `;
}

function loadExercises() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>✏️ Exercises</h1>
        <p>Bài tập thực hành để củng cố kiến thức:</p>
        <button onclick="showAvailableFiles()" class="action-btn">📄 Xem Bài Toán Thực</button>
    `;
}

function loadResources() {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = `
        <h1>🔗 Resources</h1>
        <p>Tài nguyên học tập bổ sung:</p>
        
        <div class="resources-section">
            <h3>📚 Sách</h3>
            <ul>
                <li>Pattern Recognition and Machine Learning - Bishop</li>
                <li>Deep Learning - Goodfellow, Bengio, Courville</li>
                <li>Hands-On Machine Learning - Aurélien Géron</li>
                <li>Natural Language Processing with Python - Bird, Klein, Loper</li>
            </ul>
        </div>
        
        <div class="resources-section">
            <h3>🎥 Khóa Học Online</h3>
            <ul>
                <li>Coursera: Machine Learning by Andrew Ng</li>
                <li>edX: Deep Learning Fundamentals</li>
                <li>Fast.ai: Practical Deep Learning</li>
                <li>Stanford CS231n: Computer Vision</li>
            </ul>
        </div>
        
        <div class="resources-section">
            <h3>🌐 Websites</h3>
            <ul>
                <li><a href="https://paperswithcode.com" target="_blank">Papers with Code</a></li>
                <li><a href="https://arxiv.org" target="_blank">arXiv</a></li>
                <li><a href="https://github.com/topics/machine-learning" target="_blank">GitHub ML Topics</a></li>
                <li><a href="https://kaggle.com" target="_blank">Kaggle</a></li>
            </ul>
        </div>
    `;
}

// Initialize dashboard
document.addEventListener('DOMContentLoaded', function() {
    loadOverview();
}); 