// Demo learning paths data
const learningPaths = [
  {
    id: 'basic_python',
    name: 'Lập trình Python cơ bản',
    description: 'Nắm vững kiến thức nền tảng về Python, biến, hàm, cấu trúc điều khiển, file.',
    lessons: [
      { title: 'Biến và kiểu dữ liệu', completed: true },
      { title: 'Cấu trúc điều khiển', completed: true },
      { title: 'Hàm', completed: false },
      { title: 'Xử lý file', completed: false }
    ]
  },
  {
    id: 'web_dev',
    name: 'Phát triển Web',
    description: 'Học về backend, frontend, API, database, và các công nghệ web hiện đại.',
    lessons: [
      { title: 'REST API cơ bản', completed: false },
      { title: 'Frontend cơ bản', completed: false },
      { title: 'Kết nối Database', completed: false }
    ]
  },
  {
    id: 'ml_intro',
    name: 'Nhập môn Machine Learning',
    description: 'Khám phá các khái niệm, thuật toán cơ bản trong Machine Learning.',
    lessons: [
      { title: 'Khái niệm ML', completed: true },
      { title: 'Supervised Learning', completed: false },
      { title: 'Unsupervised Learning', completed: false }
    ]
  }
];

function calcProgress(lessons) {
  if (!lessons.length) return 0;
  const done = lessons.filter(l => l.completed).length;
  return Math.round((done / lessons.length) * 100);
}

function renderStats() {
  const totalPaths = learningPaths.length;
  const totalLessons = learningPaths.reduce((sum, p) => sum + p.lessons.length, 0);
  const completedLessons = learningPaths.reduce((sum, p) => sum + p.lessons.filter(l => l.completed).length, 0);
  const percent = totalLessons ? Math.round((completedLessons / totalLessons) * 100) : 0;
  document.getElementById('stats').innerHTML = `
    <div class="stat-item"><i class="fas fa-road"></i> Lộ trình: <b>${totalPaths}</b></div>
    <div class="stat-item"><i class="fas fa-book"></i> Bài học: <b>${totalLessons}</b></div>
    <div class="stat-item"><i class="fas fa-check-circle"></i> Đã hoàn thành: <b>${completedLessons}</b></div>
    <div class="stat-item"><i class="fas fa-percent"></i> Tiến độ: <b>${percent}%</b></div>
  `;
}

function renderPaths(paths) {
  const grid = document.getElementById('path-grid');
  grid.innerHTML = '';
  paths.forEach(path => {
    const progress = calcProgress(path.lessons);
    const card = document.createElement('div');
    card.className = 'path-card';
    card.innerHTML = `
      <div class="path-title">${path.name}</div>
      <div class="path-desc">${path.description}</div>
      <div class="path-meta">
        <span><i class="fas fa-book"></i> ${path.lessons.length} bài học</span>
        <span><i class="fas fa-percent"></i> ${progress}%</span>
      </div>
      <div class="progress-bar"><div class="progress-fill" style="width:${progress}%"></div></div>
      <div class="progress-text">${progress}% hoàn thành</div>
    `;
    card.addEventListener('click', () => showPathDetail(path));
    grid.appendChild(card);
  });
}

function showPathDetail(path) {
  const modal = document.getElementById('modal');
  const body = document.getElementById('modal-body');
  const progress = calcProgress(path.lessons);
  body.innerHTML = `
    <h2>${path.name}</h2>
    <p>${path.description}</p>
    <div class="progress-bar"><div class="progress-fill" style="width:${progress}%"></div></div>
    <div class="progress-text">${progress}% hoàn thành</div>
    <div class="lesson-list">
      ${path.lessons.map((l, i) => `
        <div class="lesson-item">
          <span class="lesson-status ${l.completed ? 'completed' : 'incomplete'}">
            <i class="fas ${l.completed ? 'fa-check-circle' : 'fa-circle'}"></i>
          </span>
          <span class="lesson-title">${i + 1}. ${l.title}</span>
        </div>
      `).join('')}
    </div>
  `;
  modal.classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
  renderStats();
  renderPaths(learningPaths);
  document.getElementById('search-input').addEventListener('input', e => {
    const q = e.target.value.toLowerCase();
    const filtered = learningPaths.filter(p =>
      p.name.toLowerCase().includes(q) ||
      p.description.toLowerCase().includes(q)
    );
    renderPaths(filtered);
  });
  document.getElementById('close-modal').onclick = () => {
    document.getElementById('modal').classList.remove('active');
  };
  window.onclick = function(event) {
    if (event.target === document.getElementById('modal')) {
      document.getElementById('modal').classList.remove('active');
    }
  };
});

// AIDEV Learning Application
class AIDEVLearning {
    constructor() {
        this.currentSection = 'home';
        this.lessons = {
            'python': {
                'variables': {
                    title: 'Biến và Kiểu Dữ Liệu trong Python',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Trong bài học này, bạn sẽ học về các kiểu dữ liệu cơ bản trong Python và cách sử dụng biến.</p>
                            
                            <h4>🎯 Mục tiêu học tập</h4>
                            <ul>
                                <li>Hiểu khái niệm biến trong Python</li>
                                <li>Nắm vững các kiểu dữ liệu cơ bản</li>
                                <li>Biết cách khai báo và sử dụng biến</li>
                                <li>Hiểu về type conversion</li>
                            </ul>

                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code># Integer (Số nguyên)
age = 25
print(f"Tuổi: {age}, Kiểu: {type(age)}")

# Float (Số thực)
height = 1.75
print(f"Chiều cao: {height}, Kiểu: {type(height)}")

# String (Chuỗi)
name = "John Doe"
print(f"Tên: {name}, Kiểu: {type(name)}")

# Boolean (Luận lý)
is_student = True
print(f"Là sinh viên: {is_student}, Kiểu: {type(is_student)}")

# List (Danh sách)
fruits = ["apple", "banana", "orange"]
print(f"Trái cây: {fruits}, Kiểu: {type(fruits)}")

# Dictionary (Từ điển)
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(f"Thông tin: {person}, Kiểu: {type(person)}")</code></pre>
                            </div>

                            <h4>📝 Bài tập thực hành</h4>
                            <div class="exercise">
                                <p><strong>Bài tập 1:</strong> Tạo các biến với các kiểu dữ liệu khác nhau và in ra thông tin của chúng.</p>
                                <p><strong>Bài tập 2:</strong> Tạo một dictionary chứa thông tin cá nhân của bạn.</p>
                                <p><strong>Bài tập 3:</strong> Thực hiện các phép toán cơ bản với các kiểu dữ liệu số.</p>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-primary" onclick="markLessonComplete('python', 'variables')">
                                    <i class="fas fa-check"></i> Đánh dấu hoàn thành
                                </button>
                                <button class="btn btn-secondary" onclick="copyCode()">
                                    <i class="fas fa-copy"></i> Copy code
                                </button>
                            </div>
                        </div>
                    `
                },
                'control': {
                    title: 'Cấu Trúc Điều Khiển trong Python',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học về các cấu trúc điều khiển cơ bản trong Python: if-else, loops, và control flow.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code># If-else statement
age = 18
if age >= 18:
    print("Bạn đã trưởng thành")
else:
    print("Bạn chưa trưởng thành")

# For loop
for i in range(5):
    print(f"Số: {i}")

# While loop
count = 0
while count < 3:
    print(f"Đếm: {count}")
    count += 1</code></pre>
                            </div>

                            <h4>📝 Bài tập thực hành</h4>
                            <div class="exercise">
                                <p><strong>Bài tập 1:</strong> Viết chương trình kiểm tra số chẵn lẻ.</p>
                                <p><strong>Bài tập 2:</strong> In ra bảng cửu chương từ 1 đến 10.</p>
                                <p><strong>Bài tập 3:</strong> Tính tổng các số từ 1 đến n.</p>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-primary" onclick="markLessonComplete('python', 'control')">
                                    <i class="fas fa-check"></i> Đánh dấu hoàn thành
                                </button>
                                <button class="btn btn-secondary" onclick="copyCode()">
                                    <i class="fas fa-copy"></i> Copy code
                                </button>
                            </div>
                        </div>
                    `
                },
                'functions': {
                    title: 'Hàm và Module trong Python',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học cách tạo và sử dụng hàm, cũng như cách tổ chức code với modules.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code># Định nghĩa hàm
def greet(name):
    return f"Xin chào, {name}!"

# Sử dụng hàm
message = greet("An")
print(message)

# Hàm với tham số mặc định
def calculate_area(length, width=10):
    return length * width

# Hàm với nhiều tham số
def calculate_rectangle_area(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Sử dụng hàm trả về nhiều giá trị
area, perimeter = calculate_rectangle_area(5, 3)
print(f"Diện tích: {area}, Chu vi: {perimeter}")</code></pre>
                            </div>

                            <h4>📝 Bài tập thực hành</h4>
                            <div class="exercise">
                                <p><strong>Bài tập 1:</strong> Tạo hàm tính diện tích hình tròn.</p>
                                <p><strong>Bài tập 2:</strong> Viết hàm kiểm tra số nguyên tố.</p>
                                <p><strong>Bài tập 3:</strong> Tạo hàm tính giai thừa.</p>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-primary" onclick="markLessonComplete('python', 'functions')">
                                    <i class="fas fa-check"></i> Đánh dấu hoàn thành
                                </button>
                                <button class="btn btn-secondary" onclick="copyCode()">
                                    <i class="fas fa-copy"></i> Copy code
                                </button>
                            </div>
                        </div>
                    `
                },
                'files': {
                    title: 'Xử Lý File trong Python',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học cách đọc và ghi file trong Python.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code># Ghi file
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Xin chào thế giới!\\n")
    file.write("Đây là dòng thứ hai\\n")

# Đọc file
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# Đọc từng dòng
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(f"Dòng: {line.strip()}")</code></pre>
                            </div>

                            <h4>📝 Bài tập thực hành</h4>
                            <div class="exercise">
                                <p><strong>Bài tập 1:</strong> Tạo file và ghi danh sách tên học sinh.</p>
                                <p><strong>Bài tập 2:</strong> Đọc file và đếm số từ.</p>
                                <p><strong>Bài tập 3:</strong> Tạo chương trình ghi log.</p>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-secondary" onclick="closeModal()">
                                    <i class="fas fa-times"></i> Đóng
                                </button>
                            </div>
                        </div>
                    `
                },
                'oop': {
                    title: 'Lập Trình Hướng Đối Tượng',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học về classes, objects, inheritance và polymorphism.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code># Định nghĩa class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Tôi là {self.name}, {self.age} tuổi"

# Tạo object
person1 = Person("An", 25)
print(person1.introduce())

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        return f"{self.name} đang học bài"</code></pre>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-secondary" onclick="closeModal()">
                                    <i class="fas fa-times"></i> Đóng
                                </button>
                            </div>
                        </div>
                    `
                },
                'exceptions': {
                    title: 'Xử Lý Ngoại Lệ',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học cách xử lý lỗi và exceptions trong Python.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code># Try-except cơ bản
try:
    number = int(input("Nhập một số: "))
    result = 10 / number
    print(f"Kết quả: {result}")
except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
except Exception as e:
    print(f"Lỗi khác: {e}")</code></pre>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-secondary" onclick="closeModal()">
                                    <i class="fas fa-times"></i> Đóng
                                </button>
                            </div>
                        </div>
                    `
                }
            },
            'web': {
                'html-css': {
                    title: 'HTML & CSS Cơ Bản',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học cấu trúc HTML và styling với CSS để tạo trang web cơ bản.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Trang web đầu tiên&lt;/title&gt;
    &lt;style&gt;
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;h1&gt;Xin chào thế giới!&lt;/h1&gt;
        &lt;p&gt;Đây là trang web đầu tiên của tôi.&lt;/p&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
                            </div>

                            <h4>📝 Bài tập thực hành</h4>
                            <div class="exercise">
                                <p><strong>Bài tập 1:</strong> Tạo trang web giới thiệu bản thân.</p>
                                <p><strong>Bài tập 2:</strong> Tạo form đăng ký đơn giản.</p>
                                <p><strong>Bài tập 3:</strong> Tạo layout responsive.</p>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-primary" onclick="markLessonComplete('web', 'html-css')">
                                    <i class="fas fa-check"></i> Đánh dấu hoàn thành
                                </button>
                                <button class="btn btn-secondary" onclick="copyCode()">
                                    <i class="fas fa-copy"></i> Copy code
                                </button>
                            </div>
                        </div>
                    `
                },
                'javascript': {
                    title: 'JavaScript Cơ Bản',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Học lập trình JavaScript để tạo tương tác cho trang web.</p>
                            
                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code>// Biến và kiểu dữ liệu
let name = "An";
const age = 25;
let isStudent = true;

// Hàm
function greet(name) {
    return \`Xin chào, \${name}!\`;
}

// Event handling
document.getElementById('btn').addEventListener('click', function() {
    alert('Bạn đã click vào nút!');
});

// DOM manipulation
function changeText() {
    document.getElementById('title').innerHTML = 'Tiêu đề mới!';
}</code></pre>
                            </div>

                            <h4>📝 Bài tập thực hành</h4>
                            <div class="exercise">
                                <p><strong>Bài tập 1:</strong> Tạo máy tính đơn giản.</p>
                                <p><strong>Bài tập 2:</strong> Tạo game đoán số.</p>
                                <p><strong>Bài tập 3:</strong> Tạo todo list.</p>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-primary" onclick="markLessonComplete('web', 'javascript')">
                                    <i class="fas fa-check"></i> Đánh dấu hoàn thành
                                </button>
                                <button class="btn btn-secondary" onclick="copyCode()">
                                    <i class="fas fa-copy"></i> Copy code
                                </button>
                            </div>
                        </div>
                    `
                }
            },
            'data': {
                'intro': {
                    title: 'Giới Thiệu Data Science',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Khám phá thế giới khoa học dữ liệu và các ứng dụng thực tế.</p>
                            
                            <h4>🎯 Các chủ đề chính</h4>
                            <ul>
                                <li>Thu thập và làm sạch dữ liệu</li>
                                <li>Phân tích thống kê</li>
                                <li>Trực quan hóa dữ liệu</li>
                                <li>Machine Learning cơ bản</li>
                            </ul>

                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code>import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
data = pd.read_csv('data.csv')

# Phân tích cơ bản
print(data.head())
print(data.describe())

# Vẽ biểu đồ
data['column'].hist()
plt.title('Histogram')
plt.show()</code></pre>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-primary" onclick="markLessonComplete('data', 'intro')">
                                    <i class="fas fa-check"></i> Đánh dấu hoàn thành
                                </button>
                                <button class="btn btn-secondary" onclick="copyCode()">
                                    <i class="fas fa-copy"></i> Copy code
                                </button>
                            </div>
                        </div>
                    `
                }
            },
            'ml': {
                'intro': {
                    title: 'Giới Thiệu Machine Learning',
                    content: `
                        <div class="lesson-content">
                            <h4>📚 Tổng quan</h4>
                            <p>Khái niệm cơ bản về machine learning và các thuật toán phổ biến.</p>
                            
                            <h4>🎯 Các loại Machine Learning</h4>
                            <ul>
                                <li><strong>Supervised Learning:</strong> Học có giám sát</li>
                                <li><strong>Unsupervised Learning:</strong> Học không giám sát</li>
                                <li><strong>Reinforcement Learning:</strong> Học tăng cường</li>
                            </ul>

                            <h4>💻 Ví dụ code</h4>
                            <div class="code-block">
                                <pre><code>from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Tạo dữ liệu mẫu
X = np.random.rand(100, 1)
y = 2 * X + 1 + np.random.rand(100, 1) * 0.1

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Huấn luyện model
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
predictions = model.predict(X_test)</code></pre>
                            </div>

                            <div class="lesson-footer">
                                <button class="btn btn-secondary" onclick="closeModal()">
                                    <i class="fas fa-times"></i> Đóng
                                </button>
                            </div>
                        </div>
                    `
                }
            }
        };
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.addStyles();
    }

    setupEventListeners() {
        // Navigation tabs
        document.querySelectorAll('.nav-tab').forEach(tab => {
            tab.addEventListener('click', (e) => {
                const section = e.currentTarget.dataset.section;
                this.switchSection(section);
            });
        });

        // Modal close
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal')) {
                this.closeModal();
            }
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeModal();
            }
        });
    }

    switchSection(sectionName) {
        // Update navigation
        document.querySelectorAll('.nav-tab').forEach(tab => {
            tab.classList.remove('active');
        });
        document.querySelector(`[data-section="${sectionName}"]`).classList.add('active');

        // Update content sections
        document.querySelectorAll('.content-section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(sectionName).classList.add('active');

        this.currentSection = sectionName;
    }

    openLesson(section, lessonId) {
        const lesson = this.lessons[section]?.[lessonId];
        if (!lesson) {
            alert('Bài học chưa có sẵn!');
            return;
        }

        document.getElementById('modalTitle').textContent = lesson.title;
        document.getElementById('modalBody').innerHTML = lesson.content;
        document.getElementById('lessonModal').style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

    closeModal() {
        document.getElementById('lessonModal').style.display = 'none';
        document.body.style.overflow = 'auto';
    }

    addStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .lesson-content {
                line-height: 1.6;
            }
            
            .lesson-content h4 {
                color: #333;
                margin: 1.5rem 0 0.5rem 0;
                font-size: 1.1rem;
            }
            
            .lesson-content ul {
                margin: 1rem 0;
                padding-left: 1.5rem;
            }
            
            .lesson-content li {
                margin: 0.5rem 0;
            }
            
            .code-block {
                background: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 8px;
                padding: 1rem;
                margin: 1rem 0;
                overflow-x: auto;
            }
            
            .code-block pre {
                margin: 0;
                font-family: 'Courier New', monospace;
                font-size: 0.9rem;
                line-height: 1.4;
            }
            
            .code-block code {
                color: #333;
            }
            
            .exercise {
                background: #e3f2fd;
                border-left: 4px solid #2196f3;
                padding: 1rem;
                margin: 1rem 0;
                border-radius: 0 8px 8px 0;
            }
            
            .lesson-footer {
                display: flex;
                gap: 1rem;
                margin-top: 2rem;
                padding-top: 1rem;
                border-top: 1px solid #e9ecef;
            }
        `;
        document.head.appendChild(style);
    }
}

// Global functions
function switchSection(sectionName) {
    app.switchSection(sectionName);
}

function openLesson(section, lessonId) {
    app.openLesson(section, lessonId);
}

function closeModal() {
    app.closeModal();
}

function markLessonComplete(section, lessonId) {
    // Simulate marking lesson as complete
    const lessonCard = document.querySelector(`[onclick="openLesson('${section}', '${lessonId}')"]`);
    if (lessonCard) {
        lessonCard.classList.add('completed');
        lessonCard.classList.remove('active');
        
        // Show success message
        showNotification('Chúc mừng! Bạn đã hoàn thành bài học này.', 'success');
        closeModal();
    }
}

function copyCode() {
    const codeBlocks = document.querySelectorAll('.code-block pre code');
    let allCode = '';
    
    codeBlocks.forEach(block => {
        allCode += block.textContent + '\n\n';
    });
    
    navigator.clipboard.writeText(allCode).then(() => {
        showNotification('Đã copy code vào clipboard!', 'success');
    }).catch(() => {
        showNotification('Không thể copy code. Vui lòng copy thủ công.', 'error');
    });
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas ${getNotificationIcon(type)}"></i>
        <span>${message}</span>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${getNotificationColor(type)};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 10000;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        animation: slideInRight 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            if (document.body.contains(notification)) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

function getNotificationIcon(type) {
    const icons = {
        'success': 'fa-check-circle',
        'error': 'fa-exclamation-circle',
        'warning': 'fa-exclamation-triangle',
        'info': 'fa-info-circle'
    };
    return icons[type] || 'fa-info-circle';
}

function getNotificationColor(type) {
    const colors = {
        'success': '#28a745',
        'error': '#dc3545',
        'warning': '#ffc107',
        'info': '#17a2b8'
    };
    return colors[type] || '#17a2b8';
}

// Add CSS animations for notifications
const notificationStyle = document.createElement('style');
notificationStyle.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(notificationStyle);

// Initialize app when DOM is loaded
let app;
document.addEventListener('DOMContentLoaded', () => {
    app = new AIDEVLearning();
}); 