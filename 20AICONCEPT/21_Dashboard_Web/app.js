function loadContent(section) {
    const fileMap = {
        overview: 'overview.html',
        topics: 'topics.html',
        browse: 'browse.html',
        theory: 'theory.html',
        quiz: 'quiz.html',
        code: 'code.html',
        project: 'project.html',
        datasets: 'datasets.html',
        roadmap: 'roadmap.html',
        exercises: 'exercises.html',
        resources: 'resources.html'
    };
    const file = fileMap[section] || fileMap['overview'];
    fetch(file)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content-area').innerHTML = html;
        });
    // Đổi trạng thái active trên sidebar
    document.querySelectorAll('.sidebar nav ul li a').forEach(a => a.classList.remove('active'));
    const navLinks = document.querySelectorAll('.sidebar nav ul li a');
    const sections = ['overview','topics','browse','theory','quiz','code','project','datasets','roadmap','exercises','resources'];
    const idx = sections.indexOf(section);
    if (idx >= 0) navLinks[idx].classList.add('active');
}

// Load mặc định khi vào trang
window.onload = function() {
    loadContent('overview');
}; 