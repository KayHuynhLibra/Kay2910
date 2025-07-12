// Demo static tree data for AIDEV project
const projectTree = [
  {
    type: 'folder',
    name: 'ai_system',
    children: [
      { type: 'file', name: 'README.md' },
      { type: 'folder', name: 'agents', children: [
        { type: 'file', name: 'base_agent.py' },
        { type: 'file', name: 'chat_agent.py' },
        { type: 'file', name: 'coordinator.py' },
        { type: 'file', name: 'learning_agent.py' },
        { type: 'file', name: 'task_agent.py' }
      ] },
      { type: 'folder', name: 'api', children: [
        { type: 'file', name: 'main.py' },
        { type: 'folder', name: 'routes', children: [
          { type: 'file', name: 'chat_history.py' }
        ] }
      ] },
      { type: 'folder', name: 'core', children: [
        { type: 'file', name: 'chat_history.py' },
        { type: 'file', name: 'mcb.py' },
        { type: 'file', name: 'monitoring.py' },
        { type: 'file', name: 'scheduler.py' },
        { type: 'file', name: 'security.py' },
        { type: 'file', name: '__init__.py' }
      ] },
      { type: 'folder', name: 'config', children: [
        { type: 'file', name: 'chat_history_config.py' }
      ] },
      { type: 'folder', name: 'data', children: [
        { type: 'file', name: 'data_manager.py' }
      ] },
      { type: 'folder', name: 'models', children: [
        { type: 'file', name: 'model_manager.py' }
      ] },
      { type: 'folder', name: 'monitoring', children: [
        { type: 'file', name: 'chat_history_metrics.py' },
        { type: 'file', name: 'metrics.py' }
      ] },
      { type: 'folder', name: 'security', children: [
        { type: 'file', name: 'rate_limiter.py' },
        { type: 'file', name: 'security_manager.py' }
      ] },
      { type: 'folder', name: 'stats', children: [
        { type: 'file', name: 'README.md' },
        { type: 'file', name: 'requirements.txt' },
        { type: 'file', name: 'statistical_agent.py' }
      ] },
      { type: 'folder', name: 'tests', children: [
        { type: 'file', name: 'conftest.py' },
        { type: 'file', name: 'requirements-test.txt' },
        { type: 'folder', name: 'test_agents', children: [
          { type: 'file', name: 'test_base_agent.py' }
        ] },
        { type: 'file', name: 'test_chat_agent.py' },
        { type: 'file', name: 'test_data_manager.py' },
        { type: 'file', name: 'test_learning_agent.py' },
        { type: 'file', name: 'test_mcb.py' },
        { type: 'file', name: 'test_metrics.py' },
        { type: 'file', name: 'test_model_manager.py' },
        { type: 'file', name: 'test_rate_limiter.py' },
        { type: 'file', name: 'test_security_manager.py' }
      ] },
      { type: 'file', name: 'main.py' },
      { type: 'file', name: 'requirements.txt' }
    ]
  },
  { type: 'folder', name: 'learning', children: [
    { type: 'folder', name: '01_basic_programming', children: [
      { type: 'folder', name: 'python_basics', children: [
        { type: 'file', name: '01_variables.py' },
        { type: 'file', name: '02_control_structures.py' },
        { type: 'file', name: '03_functions.py' },
        { type: 'file', name: '04_file_handling.py' },
        { type: 'file', name: 'README.md' }
      ] },
      { type: 'file', name: 'README.md' },
      { type: 'file', name: 'requirements.txt' }
    ] },
    { type: 'folder', name: '02_web_development', children: [
      { type: 'folder', name: 'backend', children: [
        { type: 'folder', name: '01_rest_api', children: [] },
        { type: 'folder', name: '02_graphql', children: [] },
        { type: 'folder', name: '03_websockets', children: [] },
        { type: 'folder', name: '04_microservices', children: [] },
        { type: 'folder', name: '05_serverless', children: [] }
      ] },
      { type: 'folder', name: 'databases', children: [
        { type: 'folder', name: '01_sql', children: [] },
        { type: 'folder', name: '02_nosql', children: [] },
        { type: 'folder', name: '03_orm', children: [] },
        { type: 'folder', name: '04_caching', children: [] },
        { type: 'folder', name: '05_search_engines', children: [] }
      ] },
      { type: 'folder', name: 'frontend', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '03_software_engineering', children: [
      { type: 'folder', name: 'deployment', children: [] },
      { type: 'folder', name: 'design_patterns', children: [] },
      { type: 'folder', name: 'testing', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '04_data_science', children: [
      { type: 'folder', name: 'data_analysis', children: [] },
      { type: 'folder', name: 'statistics', children: [] },
      { type: 'folder', name: 'visualization', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '05_machine_learning', children: [
      { type: 'folder', name: 'deep_learning', children: [] },
      { type: 'folder', name: 'supervised_learning', children: [] },
      { type: 'folder', name: 'unsupervised_learning', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '06_natural_language', children: [
      { type: 'folder', name: 'chatbots', children: [] },
      { type: 'folder', name: 'nlp_models', children: [] },
      { type: 'folder', name: 'text_processing', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '06_natural_language_processing', children: [
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '07_computer_vision', children: [
      { type: 'folder', name: 'face_recognition', children: [] },
      { type: 'folder', name: 'image_processing', children: [] },
      { type: 'folder', name: 'object_detection', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '08_reinforcement_learning', children: [
      { type: 'folder', name: 'deep_rl', children: [] },
      { type: 'folder', name: 'policy_gradients', children: [] },
      { type: 'folder', name: 'q_learning', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '09_ai_agents', children: [
      { type: 'folder', name: 'agent_architecture', children: [] },
      { type: 'folder', name: 'autonomous_systems', children: [] },
      { type: 'folder', name: 'multi_agent', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: '10_advanced_topics', children: [
      { type: 'folder', name: 'ai_ethics', children: [] },
      { type: 'folder', name: 'generative_ai', children: [] },
      { type: 'folder', name: 'quantum_computing', children: [] },
      { type: 'file', name: 'README.md' }
    ] },
    { type: 'folder', name: 'mcb_lecture', children: [
      { type: 'file', name: 'mcb_example.py' },
      { type: 'file', name: 'README.md' },
      { type: 'file', name: 'requirements.txt' },
      { type: 'file', name: 'test_mcb.py' }
    ] },
    { type: 'folder', name: 'python_basics', children: [
      { type: 'folder', name: '01_syntax', children: [
        { type: 'file', name: 'control_flow.py' },
        { type: 'file', name: 'file_handling.py' },
        { type: 'file', name: 'functions.py' },
        { type: 'file', name: 'operators.py' },
        { type: 'file', name: 'variables.py' }
      ] },
      { type: 'folder', name: '02_oop', children: [
        { type: 'file', name: 'classes.py' },
        { type: 'file', name: 'encapsulation.py' },
        { type: 'file', name: 'inheritance.py' }
      ] },
      { type: 'folder', name: 'exercises', children: [
        { type: 'file', name: '01_variables.py' },
        { type: 'file', name: '02_control_flow.py' },
        { type: 'file', name: '03_functions.py' },
        { type: 'file', name: '04_oop.py' },
        { type: 'file', name: '05_exceptions.py' },
        { type: 'file', name: '06_files.py' },
        { type: 'file', name: '07_async.py' },
        { type: 'file', name: '08_testing.py' },
        { type: 'file', name: '09_fastapi.py' },
        { type: 'file', name: '10_docker.py' },
        { type: 'file', name: '11_cicd.py' },
        { type: 'file', name: '12_monitoring.py' },
        { type: 'file', name: '13_testing.py' },
        { type: 'file', name: '14_security.py' },
        { type: 'file', name: '15_database.py' },
        { type: 'file', name: '16_api.py' },
        { type: 'file', name: '17_async.py' },
        { type: 'file', name: '18_testing.py' },
        { type: 'file', name: '19_logging.py' },
        { type: 'file', name: '20_error_handling.py' },
        { type: 'file', name: '21_concurrency.py' },
        { type: 'file', name: '22_networking.py' },
        { type: 'file', name: '23_security.py' },
        { type: 'file', name: '24_testing.py' },
        { type: 'file', name: '25_documentation.py' },
        { type: 'file', name: '26_packaging.py' },
        { type: 'file', name: '27_deployment.py' },
        { type: 'file', name: '28_performance.py' },
        { type: 'file', name: '29_debugging.py' },
        { type: 'file', name: '30_testing.py' },
        { type: 'file', name: '31_documentation.py' },
        { type: 'file', name: '32_packaging.py' },
        { type: 'file', name: '33_deployment.py' },
        { type: 'file', name: '34_performance.py' },
        { type: 'file', name: '35_debugging.py' },
        { type: 'file', name: '36_testing.py' },
        { type: 'file', name: '37_documentation.py' },
        { type: 'file', name: '38_packaging.py' },
        { type: 'file', name: '39_deployment.py' },
        { type: 'file', name: '40_performance.py' },
        { type: 'file', name: '41_debugging.py' },
        { type: 'file', name: '42_testing.py' },
        { type: 'file', name: '43_documentation.py' },
        { type: 'file', name: '44_packaging.py' },
        { type: 'file', name: '45_deployment.py' },
        { type: 'file', name: '46_performance.py' },
        { type: 'file', name: '47_debugging.py' },
        { type: 'file', name: '48_testing.py' },
        { type: 'file', name: '49_documentation.py' },
        { type: 'file', name: '50_packaging.py' },
        { type: 'file', name: '51_deployment.py' }
      ] },
      { type: 'file', name: 'README.md' },
      { type: 'file', name: 'requirements.txt' }
    ] }
  ] },
  { type: 'folder', name: 'ai_system', children: [] },
  { type: 'folder', name: 'phase1', children: [] },
  { type: 'folder', name: 'chat_bot', children: [] },
  { type: 'folder', name: 'grafana', children: [] },
  { type: 'folder', name: 'k8s', children: [] },
  { type: 'folder', name: 'tests', children: [] },
  { type: 'folder', name: '.github', children: [] },
  { type: 'file', name: 'README.md' },
  { type: 'file', name: 'SETUP.md' },
  { type: 'file', name: 'LEARNING_PATH.md' },
  { type: 'file', name: 'PROJECT_STRUCTURE.md' },
  { type: 'file', name: 'STRUCTURE.md' },
  { type: 'file', name: 'CHANGELOG.md' },
  { type: 'file', name: 'ai_learning_path.md' },
  { type: 'file', name: 'requirements.txt' },
  { type: 'file', name: 'docker-compose.yml' },
  { type: 'file', name: 'Dockerfile' },
  { type: 'file', name: 'prometheus.yml' },
  { type: 'file', name: 'main.py' },
  { type: 'file', name: 'test_app.py' }
];

// Helper to render tree
function renderTree(tree, parent, path = '') {
  tree.forEach(node => {
    const el = document.createElement('div');
    el.className = node.type === 'folder' ? 'tree-folder' : 'tree-file';
    el.innerHTML = `<i class="fas fa-${node.type === 'folder' ? 'folder' : 'file'}"></i> <span>${node.name}</span>`;
    el.dataset.path = path + '/' + node.name;
    if (node.type === 'folder') {
      el.addEventListener('click', function(e) {
        e.stopPropagation();
        el.classList.toggle('open');
        if (childrenDiv.style.display === 'none') {
          childrenDiv.style.display = 'block';
        } else {
          childrenDiv.style.display = 'none';
        }
      });
      const childrenDiv = document.createElement('div');
      childrenDiv.className = 'tree-children';
      childrenDiv.style.display = 'none';
      renderTree(node.children || [], childrenDiv, el.dataset.path);
      el.appendChild(childrenDiv);
    } else {
      el.addEventListener('click', function(e) {
        e.stopPropagation();
        showFileContent(node, el.dataset.path);
      });
    }
    parent.appendChild(el);
  });
}

// Show file content (demo: just show file name and path)
function showFileContent(node, path) {
  document.getElementById('file-meta').textContent = `${node.type.toUpperCase()}: ${path}`;
  document.getElementById('file-content').textContent = `File: ${node.name}\nPath: ${path}\n\n(Demo: Nội dung file sẽ hiển thị ở đây)`;
}

// Render stats
function renderStats(tree) {
  let fileCount = 0, folderCount = 0;
  function count(tree) {
    tree.forEach(node => {
      if (node.type === 'folder') {
        folderCount++;
        count(node.children || []);
      } else {
        fileCount++;
      }
    });
  }
  count(tree);
  const statsDiv = document.getElementById('stats');
  statsDiv.innerHTML = `
    <div class="stat-item"><i class="fas fa-folder"></i> Folders: <b>${folderCount}</b></div>
    <div class="stat-item"><i class="fas fa-file"></i> Files: <b>${fileCount}</b></div>
    <div class="stat-item"><i class="fas fa-database"></i> Total: <b>${fileCount + folderCount}</b></div>
  `;
}

// Search functionality
function searchTree(tree, query) {
  if (!query) return tree;
  const q = query.toLowerCase();
  function filter(nodes) {
    return nodes
      .map(node => {
        if (node.type === 'folder') {
          const filteredChildren = filter(node.children || []);
          if (node.name.toLowerCase().includes(q) || filteredChildren.length > 0) {
            return { ...node, children: filteredChildren };
          }
        } else if (node.name.toLowerCase().includes(q)) {
          return node;
        }
        return null;
      })
      .filter(Boolean);
  }
  return filter(tree);
}

document.addEventListener('DOMContentLoaded', () => {
  const treeView = document.getElementById('tree-view');
  const searchInput = document.getElementById('search-input');
  renderTree(projectTree, treeView);
  renderStats(projectTree);

  searchInput.addEventListener('input', e => {
    treeView.innerHTML = '';
    const filtered = searchTree(projectTree, e.target.value);
    renderTree(filtered, treeView);
  });
}); 