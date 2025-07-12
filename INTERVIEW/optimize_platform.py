#!/usr/bin/env python3
"""
Script để tối ưu hóa toàn bộ Algorithm Ecosystem Platform
Tích hợp CSS và JS chung, cải thiện hiệu suất và trải nghiệm người dùng
"""

import os
import re
from pathlib import Path
import shutil

class PlatformOptimizer:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.ui_dir = self.base_dir / "AlgorithmEcosystem" / "ui"
        self.shared_dir = self.ui_dir / "shared"
        
        # Tạo thư mục shared nếu chưa có
        self.shared_dir.mkdir(exist_ok=True)
        
        # Danh sách các file CSS và JS đã tạo
        self.shared_files = {
            'styles.css': 'AlgorithmEcosystem/ui/shared/styles.css',
            'components.css': 'AlgorithmEcosystem/ui/shared/components.css',
            'animations.css': 'AlgorithmEcosystem/ui/shared/animations.css',
            'accessibility.css': 'AlgorithmEcosystem/ui/shared/accessibility.css',
            'utilities.css': 'AlgorithmEcosystem/ui/shared/utilities.css',
            'scripts.js': 'AlgorithmEcosystem/ui/shared/scripts.js'
        }

    def optimize_html_file(self, file_path):
        """Tối ưu hóa file HTML"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Thêm link đến các file CSS chung
            content = self.add_shared_css_links(content)
            
            # 2. Thêm script đến file JS chung
            content = self.add_shared_js_script(content)
            
            # 3. Thêm meta tags tối ưu
            content = self.add_optimized_meta_tags(content)
            
            # 4. Thêm preload cho critical resources
            content = self.add_preload_tags(content)
            
            # 5. Tối ưu hóa inline styles
            content = self.optimize_inline_styles(content)
            
            # 6. Thêm lazy loading cho images
            content = self.add_lazy_loading(content)
            
            # 7. Thêm service worker (nếu cần)
            content = self.add_service_worker(content)
            
            # 8. Thêm PWA manifest
            content = self.add_pwa_manifest(content)
            
            # 9. Thêm structured data
            content = self.add_structured_data(content)
            
            # 10. Tối ưu hóa performance
            content = self.optimize_performance(content)
            
            # Ghi file nếu có thay đổi
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
            
            return False
            
        except Exception as e:
            print(f"  ✗ Lỗi tối ưu {file_path.name}: {e}")
            return False

    def add_shared_css_links(self, content):
        """Thêm link đến các file CSS chung"""
        # Tìm thẻ head
        head_pattern = r'(<head[^>]*>)'
        head_match = re.search(head_pattern, content)
        
        if head_match:
            head_start = head_match.end()
            
            # CSS links
            css_links = """
    <!-- Shared CSS Files -->
    <link rel="stylesheet" href="shared/styles.css">
    <link rel="stylesheet" href="shared/components.css">
    <link rel="stylesheet" href="shared/animations.css">
    <link rel="stylesheet" href="shared/accessibility.css">
    <link rel="stylesheet" href="shared/utilities.css">
"""
            
            # Điều chỉnh đường dẫn dựa trên vị trí file
            relative_path = self.get_relative_path_to_shared()
            css_links = css_links.replace('shared/', f'{relative_path}shared/')
            
            content = content[:head_start] + css_links + content[head_start:]
        
        return content

    def add_shared_js_script(self, content):
        """Thêm script đến file JS chung"""
        # Tìm thẻ body
        body_pattern = r'(</body>)'
        body_match = re.search(body_pattern, content)
        
        if body_match:
            body_end = body_match.start()
            
            # JS script
            js_script = """
    <!-- Shared JavaScript -->
    <script src="shared/scripts.js"></script>
"""
            
            # Điều chỉnh đường dẫn dựa trên vị trí file
            relative_path = self.get_relative_path_to_shared()
            js_script = js_script.replace('shared/', f'{relative_path}shared/')
            
            content = content[:body_end] + js_script + content[body_end:]
        
        return content

    def add_optimized_meta_tags(self, content):
        """Thêm meta tags tối ưu"""
        head_pattern = r'(<head[^>]*>)'
        head_match = re.search(head_pattern, content)
        
        if head_match:
            head_start = head_match.end()
            
            # Meta tags tối ưu
            meta_tags = """
    <!-- Performance & SEO Meta Tags -->
    <meta name="description" content="Algorithm Ecosystem Platform - Học thuật toán hiệu quả với công cụ tương tác">
    <meta name="keywords" content="algorithms, data structures, programming, learning, interactive">
    <meta name="author" content="Algorithm Ecosystem Platform">
    <meta name="robots" content="index, follow">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Algorithm Ecosystem Platform">
    <meta property="og:description" content="Học thuật toán hiệu quả với công cụ tương tác">
    <meta property="og:type" content="website">
    <meta property="og:url" content="">
    <meta property="og:image" content="">
    
    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Algorithm Ecosystem Platform">
    <meta name="twitter:description" content="Học thuật toán hiệu quả với công cụ tương tác">
    
    <!-- Performance Meta Tags -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="format-detection" content="telephone=no">
    <meta name="theme-color" content="#667eea">
    <meta name="msapplication-TileColor" content="#667eea">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Algorithm Ecosystem">
"""
            
            content = content[:head_start] + meta_tags + content[head_start:]
        
        return content

    def add_preload_tags(self, content):
        """Thêm preload tags cho critical resources"""
        head_pattern = r'(<head[^>]*>)'
        head_match = re.search(head_pattern, content)
        
        if head_match:
            head_start = head_match.end()
            
            # Preload tags
            preload_tags = """
    <!-- Preload Critical Resources -->
    <link rel="preload" href="shared/styles.css" as="style">
    <link rel="preload" href="shared/scripts.js" as="script">
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style">
    <link rel="dns-prefetch" href="//fonts.googleapis.com">
    <link rel="dns-prefetch" href="//cdn.jsdelivr.net">
    <link rel="dns-prefetch" href="//cdnjs.cloudflare.com">
"""
            
            # Điều chỉnh đường dẫn
            relative_path = self.get_relative_path_to_shared()
            preload_tags = preload_tags.replace('shared/', f'{relative_path}shared/')
            
            content = content[:head_start] + preload_tags + content[head_start:]
        
        return content

    def optimize_inline_styles(self, content):
        """Tối ưu hóa inline styles"""
        # Loại bỏ các style trùng lặp hoặc không cần thiết
        # Giữ lại các style quan trọng và chuyển phần còn lại vào file CSS chung
        
        # Tìm và xóa các style block lớn
        style_pattern = r'<style[^>]*>(.*?)</style>'
        style_matches = re.findall(style_pattern, content, re.DOTALL)
        
        for style_content in style_matches:
            if len(style_content) > 1000:  # Chỉ xóa style block lớn
                content = content.replace(f'<style>{style_content}</style>', '')
        
        return content

    def add_lazy_loading(self, content):
        """Thêm lazy loading cho images"""
        # Thêm loading="lazy" cho tất cả images
        img_pattern = r'<img([^>]*)>'
        
        def add_lazy_loading(match):
            img_tag = match.group(0)
            if 'loading=' not in img_tag:
                img_tag = img_tag.replace('<img', '<img loading="lazy"')
            return img_tag
        
        content = re.sub(img_pattern, add_lazy_loading, content)
        
        return content

    def add_service_worker(self, content):
        """Thêm service worker"""
        body_pattern = r'(</body>)'
        body_match = re.search(body_pattern, content)
        
        if body_match:
            body_end = body_match.start()
            
            service_worker_script = """
    <!-- Service Worker Registration -->
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('sw.js')
                    .then(function(registration) {
                        console.log('ServiceWorker registration successful');
                    })
                    .catch(function(err) {
                        console.log('ServiceWorker registration failed');
                    });
            });
        }
    </script>
"""
            
            content = content[:body_end] + service_worker_script + content[body_end:]
        
        return content

    def add_pwa_manifest(self, content):
        """Thêm PWA manifest"""
        head_pattern = r'(<head[^>]*>)'
        head_match = re.search(head_pattern, content)
        
        if head_match:
            head_start = head_match.end()
            
            manifest_links = """
    <!-- PWA Manifest -->
    <link rel="manifest" href="manifest.json">
    <link rel="icon" type="image/png" sizes="32x32" href="icons/icon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="icons/icon-16x16.png">
    <link rel="apple-touch-icon" href="icons/icon-192x192.png">
"""
            
            content = content[:head_start] + manifest_links + content[head_start:]
        
        return content

    def add_structured_data(self, content):
        """Thêm structured data"""
        head_pattern = r'(<head[^>]*>)'
        head_match = re.search(head_pattern, content)
        
        if head_match:
            head_start = head_match.end()
            
            structured_data = """
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Algorithm Ecosystem Platform",
        "description": "Interactive platform for learning algorithms and data structures",
        "url": "",
        "applicationCategory": "EducationalApplication",
        "operatingSystem": "Web Browser",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        }
    }
    </script>
"""
            
            content = content[:head_start] + structured_data + content[head_start:]
        
        return content

    def optimize_performance(self, content):
        """Tối ưu hóa performance"""
        # Thêm các thuộc tính performance
        content = content.replace('<script', '<script defer')
        content = content.replace('<link rel="stylesheet"', '<link rel="stylesheet" media="print" onload="this.media=\'all\'"')
        
        return content

    def get_relative_path_to_shared(self):
        """Lấy đường dẫn tương đối đến thư mục shared"""
        # Đây là một ước tính đơn giản, có thể cần điều chỉnh
        return "../"

    def create_service_worker(self):
        """Tạo service worker"""
        sw_content = """
// Algorithm Ecosystem Platform Service Worker
const CACHE_NAME = 'algorithm-ecosystem-v1';
const urlsToCache = [
    '/',
    '/shared/styles.css',
    '/shared/components.css',
    '/shared/animations.css',
    '/shared/accessibility.css',
    '/shared/utilities.css',
    '/shared/scripts.js'
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});
"""
        
        sw_path = self.base_dir / "sw.js"
        with open(sw_path, 'w', encoding='utf-8') as f:
            f.write(sw_content)

    def create_manifest(self):
        """Tạo PWA manifest"""
        manifest_content = {
            "name": "Algorithm Ecosystem Platform",
            "short_name": "AlgoEco",
            "description": "Interactive platform for learning algorithms and data structures",
            "start_url": "/",
            "display": "standalone",
            "background_color": "#667eea",
            "theme_color": "#667eea",
            "icons": [
                {
                    "src": "icons/icon-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png"
                },
                {
                    "src": "icons/icon-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png"
                }
            ]
        }
        
        import json
        manifest_path = self.base_dir / "manifest.json"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest_content, f, indent=2)

    def create_icons_directory(self):
        """Tạo thư mục icons"""
        icons_dir = self.base_dir / "icons"
        icons_dir.mkdir(exist_ok=True)
        
        # Tạo file placeholder cho icons
        icon_files = ["icon-16x16.png", "icon-32x32.png", "icon-192x192.png", "icon-512x512.png"]
        for icon_file in icon_files:
            icon_path = icons_dir / icon_file
            if not icon_path.exists():
                # Tạo file placeholder
                with open(icon_path, 'w') as f:
                    f.write("# Placeholder for icon file")

    def optimize_all_files(self):
        """Tối ưu hóa tất cả file HTML"""
        print("🚀 Bắt đầu tối ưu hóa Algorithm Ecosystem Platform...")
        print("=" * 60)
        
        # Tạo các file cần thiết
        self.create_service_worker()
        self.create_manifest()
        self.create_icons_directory()
        
        # Tìm tất cả file HTML
        html_files = []
        for root, dirs, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith('.html'):
                    html_files.append(Path(root) / file)
        
        if not html_files:
            print("❌ Không tìm thấy file HTML nào!")
            return
        
        print(f"📁 Tìm thấy {len(html_files)} file HTML:")
        
        success_count = 0
        skip_count = 0
        error_count = 0
        
        for html_file in html_files:
            print(f"\n📄 Tối ưu hóa: {html_file}")
            
            try:
                if self.optimize_html_file(html_file):
                    success_count += 1
                    print(f"  ✓ {html_file.name} - Đã tối ưu hóa")
                else:
                    skip_count += 1
                    print(f"  ⚠ {html_file.name} - Không có thay đổi")
            except Exception as e:
                error_count += 1
                print(f"  ✗ {html_file.name} - Lỗi: {e}")
        
        print("\n" + "=" * 60)
        print("📊 Kết quả tối ưu hóa:")
        print(f"  ✓ Thành công: {success_count} file")
        print(f"  ⚠ Bỏ qua: {skip_count} file")
        print(f"  ✗ Lỗi: {error_count} file")
        print(f"  📁 Tổng cộng: {len(html_files)} file")
        
        if success_count > 0:
            print("\n🎉 Hoàn thành tối ưu hóa!")
            print("💡 Các cải tiến đã được áp dụng:")
            print("   • Tích hợp CSS và JS chung")
            print("   • Thêm meta tags SEO")
            print("   • Tối ưu hóa performance")
            print("   • Thêm lazy loading")
            print("   • Hỗ trợ PWA")
            print("   • Service worker caching")
            print("   • Structured data")
            print("   • Accessibility improvements")

def main():
    """Hàm chính"""
    optimizer = PlatformOptimizer()
    optimizer.optimize_all_files()

if __name__ == "__main__":
    main() 