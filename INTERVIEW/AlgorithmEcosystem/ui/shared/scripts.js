/**
 * Algorithm Ecosystem Platform - Shared JavaScript
 * Optimized and unified functionality for all pages
 */

// Global configuration
const CONFIG = {
    // API endpoints (if any)
    API_BASE_URL: '',
    
    // Local storage keys
    STORAGE_KEYS: {
        THEME: 'algorithm_ecosystem_theme',
        PROGRESS: 'algorithm_ecosystem_progress',
        SETTINGS: 'algorithm_ecosystem_settings',
        LAST_VISITED: 'algorithm_ecosystem_last_visited'
    },
    
    // Animation durations
    ANIMATION_DURATION: 300,
    
    // Breakpoints
    BREAKPOINTS: {
        MOBILE: 768,
        TABLET: 1024,
        DESKTOP: 1200
    }
};

// Utility functions
const Utils = {
    /**
     * Debounce function to limit function calls
     */
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    /**
     * Throttle function to limit function calls
     */
    throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    /**
     * Generate unique ID
     */
    generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    },

    /**
     * Format number with commas
     */
    formatNumber(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },

    /**
     * Format date
     */
    formatDate(date) {
        return new Intl.DateTimeFormat('vi-VN', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        }).format(date);
    },

    /**
     * Check if element is in viewport
     */
    isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    },

    /**
     * Smooth scroll to element
     */
    scrollToElement(element, offset = 0) {
        const elementPosition = element.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    },

    /**
     * Copy text to clipboard
     */
    async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch (err) {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            return true;
        }
    },

    /**
     * Show notification
     */
    showNotification(message, type = 'info', duration = 3000) {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;

        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : type === 'warning' ? '#ffc107' : '#17a2b8'};
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 9999;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            max-width: 300px;
        `;

        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);

        // Close button
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        });

        // Auto remove
        setTimeout(() => {
            if (document.body.contains(notification)) {
                notification.style.transform = 'translateX(100%)';
                setTimeout(() => {
                    if (document.body.contains(notification)) {
                        document.body.removeChild(notification);
                    }
                }, 300);
            }
        }, duration);
    }
};

// Local Storage Manager
const StorageManager = {
    /**
     * Set item in localStorage
     */
    set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (error) {
            console.error('Error saving to localStorage:', error);
            return false;
        }
    },

    /**
     * Get item from localStorage
     */
    get(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (error) {
            console.error('Error reading from localStorage:', error);
            return defaultValue;
        }
    },

    /**
     * Remove item from localStorage
     */
    remove(key) {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (error) {
            console.error('Error removing from localStorage:', error);
            return false;
        }
    },

    /**
     * Clear all localStorage
     */
    clear() {
        try {
            localStorage.clear();
            return true;
        } catch (error) {
            console.error('Error clearing localStorage:', error);
            return false;
        }
    }
};

// Theme Manager
const ThemeManager = {
    /**
     * Initialize theme
     */
    init() {
        const savedTheme = StorageManager.get(CONFIG.STORAGE_KEYS.THEME, 'light');
        this.setTheme(savedTheme);
        this.createThemeToggle();
    },

    /**
     * Set theme
     */
    setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        StorageManager.set(CONFIG.STORAGE_KEYS.THEME, theme);
        
        // Update theme toggle button if exists
        const themeToggle = document.querySelector('.theme-toggle');
        if (themeToggle) {
            themeToggle.innerHTML = theme === 'dark' ? '☀️' : '🌙';
            themeToggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
        }
    },

    /**
     * Toggle theme
     */
    toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        this.setTheme(newTheme);
    },

    /**
     * Create theme toggle button
     */
    createThemeToggle() {
        const existingToggle = document.querySelector('.theme-toggle');
        if (existingToggle) return;

        const themeToggle = document.createElement('button');
        themeToggle.className = 'theme-toggle';
        themeToggle.setAttribute('aria-label', 'Toggle theme');
        themeToggle.innerHTML = document.documentElement.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';
        
        themeToggle.addEventListener('click', () => {
            this.toggleTheme();
        });

        document.body.appendChild(themeToggle);
    }
};

// Progress Manager
const ProgressManager = {
    /**
     * Initialize progress tracking
     */
    init() {
        this.loadProgress();
        this.setupProgressTracking();
    },

    /**
     * Load progress from localStorage
     */
    loadProgress() {
        const progress = StorageManager.get(CONFIG.STORAGE_KEYS.PROGRESS, {
            completed: [],
            inProgress: [],
            scores: {},
            lastUpdated: new Date().toISOString()
        });
        
        this.progress = progress;
        this.updateProgressDisplay();
    },

    /**
     * Save progress to localStorage
     */
    saveProgress() {
        this.progress.lastUpdated = new Date().toISOString();
        StorageManager.set(CONFIG.STORAGE_KEYS.PROGRESS, this.progress);
    },

    /**
     * Mark algorithm as completed
     */
    markCompleted(algorithmId) {
        if (!this.progress.completed.includes(algorithmId)) {
            this.progress.completed.push(algorithmId);
            this.saveProgress();
            this.updateProgressDisplay();
        }
    },

    /**
     * Mark algorithm as in progress
     */
    markInProgress(algorithmId) {
        if (!this.progress.inProgress.includes(algorithmId)) {
            this.progress.inProgress.push(algorithmId);
            this.saveProgress();
            this.updateProgressDisplay();
        }
    },

    /**
     * Update score for algorithm
     */
    updateScore(algorithmId, score) {
        this.progress.scores[algorithmId] = score;
        this.saveProgress();
        this.updateProgressDisplay();
    },

    /**
     * Setup progress tracking
     */
    setupProgressTracking() {
        // Track algorithm views
        document.addEventListener('click', (e) => {
            const algorithmLink = e.target.closest('[data-algorithm-id]');
            if (algorithmLink) {
                const algorithmId = algorithmLink.dataset.algorithmId;
                this.markInProgress(algorithmId);
            }
        });

        // Track completion events
        document.addEventListener('algorithmCompleted', (e) => {
            const { algorithmId, score } = e.detail;
            this.markCompleted(algorithmId);
            if (score !== undefined) {
                this.updateScore(algorithmId, score);
            }
        });
    },

    /**
     * Update progress display
     */
    updateProgressDisplay() {
        const progressElements = document.querySelectorAll('[data-progress-type]');
        
        progressElements.forEach(element => {
            const type = element.dataset.progressType;
            let value = 0;
            
            switch (type) {
                case 'completed':
                    value = this.progress.completed.length;
                    break;
                case 'in-progress':
                    value = this.progress.inProgress.length;
                    break;
                case 'total':
                    value = this.progress.completed.length + this.progress.inProgress.length;
                    break;
                case 'percentage':
                    const total = this.progress.completed.length + this.progress.inProgress.length;
                    value = total > 0 ? Math.round((this.progress.completed.length / total) * 100) : 0;
                    break;
            }
            
            element.textContent = value;
        });
    }
};

// Search Manager
const SearchManager = {
    /**
     * Initialize search functionality
     */
    init() {
        this.setupSearchInputs();
        this.setupFilters();
    },

    /**
     * Setup search inputs
     */
    setupSearchInputs() {
        const searchInputs = document.querySelectorAll('.search-input, [data-search]');
        
        searchInputs.forEach(input => {
            const debouncedSearch = Utils.debounce((query) => {
                this.performSearch(query, input);
            }, 300);

            input.addEventListener('input', (e) => {
                debouncedSearch(e.target.value);
            });

            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.performSearch(e.target.value, input);
                }
            });
        });
    },

    /**
     * Perform search
     */
    performSearch(query, input) {
        const searchContainer = input.closest('[data-search-container]') || document;
        const searchableElements = searchContainer.querySelectorAll('[data-searchable]');
        
        if (!query.trim()) {
            // Show all elements
            searchableElements.forEach(element => {
                element.style.display = '';
                element.classList.remove('search-hidden');
            });
            return;
        }

        const searchTerms = query.toLowerCase().split(' ').filter(term => term.length > 0);
        
        searchableElements.forEach(element => {
            const searchableText = element.dataset.searchable || element.textContent;
            const text = searchableText.toLowerCase();
            
            const matches = searchTerms.every(term => text.includes(term));
            
            if (matches) {
                element.style.display = '';
                element.classList.remove('search-hidden');
                this.highlightMatches(element, searchTerms);
            } else {
                element.style.display = 'none';
                element.classList.add('search-hidden');
            }
        });

        // Update search results count
        this.updateSearchResultsCount(searchContainer, query);
    },

    /**
     * Highlight search matches
     */
    highlightMatches(element, searchTerms) {
        const text = element.textContent;
        let highlightedText = text;
        
        searchTerms.forEach(term => {
            const regex = new RegExp(`(${term})`, 'gi');
            highlightedText = highlightedText.replace(regex, '<mark>$1</mark>');
        });
        
        if (highlightedText !== text) {
            element.innerHTML = highlightedText;
        }
    },

    /**
     * Update search results count
     */
    updateSearchResultsCount(container, query) {
        const countElement = container.querySelector('[data-search-count]');
        if (countElement) {
            const visibleElements = container.querySelectorAll('[data-searchable]:not(.search-hidden)');
            const totalElements = container.querySelectorAll('[data-searchable]');
            
            countElement.textContent = `${visibleElements.length} of ${totalElements.length} results`;
        }
    },

    /**
     * Setup filters
     */
    setupFilters() {
        const filterInputs = document.querySelectorAll('[data-filter]');
        
        filterInputs.forEach(input => {
            input.addEventListener('change', () => {
                this.applyFilters();
            });
        });
    },

    /**
     * Apply filters
     */
    applyFilters() {
        const filterInputs = document.querySelectorAll('[data-filter]');
        const filterableElements = document.querySelectorAll('[data-filterable]');
        
        const activeFilters = {};
        
        filterInputs.forEach(input => {
            if (input.checked) {
                const filterType = input.dataset.filter;
                const filterValue = input.value;
                
                if (!activeFilters[filterType]) {
                    activeFilters[filterType] = [];
                }
                activeFilters[filterType].push(filterValue);
            }
        });

        filterableElements.forEach(element => {
            let shouldShow = true;
            
            Object.keys(activeFilters).forEach(filterType => {
                const elementValue = element.dataset[filterType];
                if (elementValue && !activeFilters[filterType].includes(elementValue)) {
                    shouldShow = false;
                }
            });
            
            element.style.display = shouldShow ? '' : 'none';
        });
    }
};

// Modal Manager
const ModalManager = {
    /**
     * Initialize modal functionality
     */
    init() {
        this.setupModalTriggers();
        this.setupModalClose();
    },

    /**
     * Setup modal triggers
     */
    setupModalTriggers() {
        document.addEventListener('click', (e) => {
            const trigger = e.target.closest('[data-modal]');
            if (trigger) {
                e.preventDefault();
                const modalId = trigger.dataset.modal;
                this.openModal(modalId);
            }
        });
    },

    /**
     * Setup modal close
     */
    setupModalClose() {
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal') || e.target.classList.contains('modal-close')) {
                this.closeModal(e.target.closest('.modal'));
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                const openModal = document.querySelector('.modal.show');
                if (openModal) {
                    this.closeModal(openModal);
                }
            }
        });
    },

    /**
     * Open modal
     */
    openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('show');
            document.body.style.overflow = 'hidden';
            
            // Focus first focusable element
            const firstFocusable = modal.querySelector('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
            if (firstFocusable) {
                firstFocusable.focus();
            }
        }
    },

    /**
     * Close modal
     */
    closeModal(modal) {
        if (modal) {
            modal.classList.remove('show');
            document.body.style.overflow = '';
        }
    }
};

// Keyboard Shortcuts Manager
const KeyboardManager = {
    /**
     * Initialize keyboard shortcuts
     */
    init() {
        this.setupShortcuts();
        this.showShortcutsHelp();
    },

    /**
     * Setup keyboard shortcuts
     */
    setupShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Don't trigger shortcuts when typing in input fields
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
                return;
            }

            const key = e.key.toLowerCase();
            const ctrl = e.ctrlKey;
            const shift = e.shiftKey;
            const alt = e.altKey;

            // Navigation shortcuts
            if (key === 'h' && !ctrl && !shift && !alt) {
                e.preventDefault();
                window.location.href = 'index.html';
            }

            if (key === 'a' && !ctrl && !shift && !alt) {
                e.preventDefault();
                window.location.href = 'analyzers/algorithm_analyzer.html';
            }

            if (key === 'l' && !ctrl && !shift && !alt) {
                e.preventDefault();
                window.location.href = 'learning/learning_accelerator.html';
            }

            // Search shortcut
            if (key === 'f' && ctrl) {
                e.preventDefault();
                const searchInput = document.querySelector('.search-input');
                if (searchInput) {
                    searchInput.focus();
                    searchInput.select();
                }
            }

            // Theme toggle
            if (key === 't' && ctrl) {
                e.preventDefault();
                ThemeManager.toggleTheme();
            }

            // Help shortcut
            if (key === '?' && !ctrl && !shift && !alt) {
                e.preventDefault();
                this.showShortcutsHelp();
            }
        });
    },

    /**
     * Show keyboard shortcuts help
     */
    showShortcutsHelp() {
        const shortcuts = [
            { key: 'H', description: 'Go to Home' },
            { key: 'A', description: 'Go to Algorithm Analyzer' },
            { key: 'L', description: 'Go to Learning Accelerator' },
            { key: 'Ctrl + F', description: 'Focus search' },
            { key: 'Ctrl + T', description: 'Toggle theme' },
            { key: '?', description: 'Show this help' },
            { key: 'Escape', description: 'Close modal' }
        ];

        const helpHtml = `
            <div class="modal" id="shortcuts-help">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 class="modal-title">⌨️ Keyboard Shortcuts</h3>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="shortcuts-list">
                            ${shortcuts.map(shortcut => `
                                <div class="shortcut-item">
                                    <kbd class="shortcut-key">${shortcut.key}</kbd>
                                    <span class="shortcut-description">${shortcut.description}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Add styles for shortcuts help
        const style = document.createElement('style');
        style.textContent = `
            .shortcuts-list {
                display: grid;
                gap: 10px;
            }
            .shortcut-item {
                display: flex;
                align-items: center;
                gap: 15px;
                padding: 10px;
                background: #f8f9fa;
                border-radius: 8px;
            }
            .shortcut-key {
                background: #e9ecef;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 4px 8px;
                font-family: monospace;
                font-size: 0.9em;
                min-width: 60px;
                text-align: center;
            }
            .shortcut-description {
                font-weight: 500;
            }
        `;
        document.head.appendChild(style);

        // Remove existing help modal
        const existingHelp = document.getElementById('shortcuts-help');
        if (existingHelp) {
            existingHelp.remove();
        }

        // Add new help modal
        document.body.insertAdjacentHTML('beforeend', helpHtml);
        ModalManager.openModal('shortcuts-help');
    }
};

// Performance Monitor
const PerformanceMonitor = {
    /**
     * Initialize performance monitoring
     */
    init() {
        this.monitorPageLoad();
        this.monitorUserInteractions();
    },

    /**
     * Monitor page load performance
     */
    monitorPageLoad() {
        window.addEventListener('load', () => {
            const loadTime = performance.now();
            const navigation = performance.getEntriesByType('navigation')[0];
            
            console.log('Page load performance:', {
                totalLoadTime: loadTime,
                domContentLoaded: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
                loadEvent: navigation.loadEventEnd - navigation.loadEventStart
            });
        });
    },

    /**
     * Monitor user interactions
     */
    monitorUserInteractions() {
        let interactionCount = 0;
        const interactionEvents = ['click', 'keydown', 'scroll', 'input'];
        
        interactionEvents.forEach(eventType => {
            document.addEventListener(eventType, Utils.throttle(() => {
                interactionCount++;
                
                // Log every 10 interactions
                if (interactionCount % 10 === 0) {
                    console.log(`User interactions: ${interactionCount}`);
                }
            }, 1000));
        });
    }
};

// Main Application Class
class AlgorithmEcosystemApp {
    constructor() {
        this.initialized = false;
    }

    /**
     * Initialize the application
     */
    init() {
        if (this.initialized) return;

        try {
            // Initialize all managers
            ThemeManager.init();
            ProgressManager.init();
            SearchManager.init();
            ModalManager.init();
            KeyboardManager.init();
            PerformanceMonitor.init();

            // Setup global event listeners
            this.setupGlobalEvents();

            // Mark as initialized
            this.initialized = true;

            console.log('🚀 Algorithm Ecosystem Platform initialized successfully!');
            
            // Show welcome message for first-time users
            this.showWelcomeMessage();

        } catch (error) {
            console.error('Error initializing Algorithm Ecosystem Platform:', error);
        }
    }

    /**
     * Setup global event listeners
     */
    setupGlobalEvents() {
        // Handle back button
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('back-button')) {
                e.preventDefault();
                this.handleBackNavigation();
            }
        });

        // Handle copy code buttons
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('copy-code')) {
                e.preventDefault();
                this.handleCopyCode(e.target);
            }
        });

        // Handle algorithm completion
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('complete-algorithm')) {
                e.preventDefault();
                this.handleAlgorithmCompletion(e.target);
            }
        });

        // Handle smooth scrolling for anchor links
        document.addEventListener('click', (e) => {
            const link = e.target.closest('a[href^="#"]');
            if (link) {
                e.preventDefault();
                const targetId = link.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    Utils.scrollToElement(targetElement, 80);
                }
            }
        });
    }

    /**
     * Handle back navigation
     */
    handleBackNavigation() {
        const referrer = document.referrer;
        const currentPath = window.location.pathname;
        
        // If we have a referrer and it's from our domain, go back
        if (referrer && referrer.includes(window.location.hostname)) {
            window.history.back();
        } else {
            // Otherwise go to navigation hub
            window.location.href = 'index.html';
        }
    }

    /**
     * Handle copy code functionality
     */
    async handleCopyCode(button) {
        const codeBlock = button.closest('.code-section').querySelector('.code-content');
        const code = codeBlock.textContent;
        
        const success = await Utils.copyToClipboard(code);
        
        if (success) {
            const originalText = button.textContent;
            button.textContent = '✓ Copied!';
            button.classList.add('btn-success');
            
            setTimeout(() => {
                button.textContent = originalText;
                button.classList.remove('btn-success');
            }, 2000);
            
            Utils.showNotification('Code copied to clipboard!', 'success');
        } else {
            Utils.showNotification('Failed to copy code', 'error');
        }
    }

    /**
     * Handle algorithm completion
     */
    handleAlgorithmCompletion(button) {
        const algorithmId = button.dataset.algorithmId;
        const score = parseInt(button.dataset.score) || 100;
        
        // Dispatch custom event
        const event = new CustomEvent('algorithmCompleted', {
            detail: { algorithmId, score }
        });
        document.dispatchEvent(event);
        
        // Update button
        button.textContent = '✓ Completed!';
        button.classList.add('btn-success');
        button.disabled = true;
        
        Utils.showNotification('Algorithm completed! Great job! 🎉', 'success');
    }

    /**
     * Show welcome message for first-time users
     */
    showWelcomeMessage() {
        const hasVisited = StorageManager.get('has_visited_before', false);
        
        if (!hasVisited) {
            StorageManager.set('has_visited_before', true);
            
            setTimeout(() => {
                Utils.showNotification(
                    'Welcome to Algorithm Ecosystem Platform! 🚀 Use ? to see keyboard shortcuts.',
                    'info',
                    5000
                );
            }, 1000);
        }
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const app = new AlgorithmEcosystemApp();
    app.init();
});

// Export for use in other scripts
window.AlgorithmEcosystem = {
    Utils,
    StorageManager,
    ThemeManager,
    ProgressManager,
    SearchManager,
    ModalManager,
    KeyboardManager,
    PerformanceMonitor,
    CONFIG
}; 