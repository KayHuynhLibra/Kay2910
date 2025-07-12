#!/usr/bin/env python3
"""
Script to optimize all HTML files in the Algorithm Ecosystem
- Fix CSS/JS paths
- Add missing meta tags
- Ensure proper navigation
- Add service worker registration
"""

import os
import re
from pathlib import Path

def fix_html_file(file_path):
    """Fix a single HTML file"""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix CSS paths
        content = re.sub(r'href="\.\./shared/', 'href="shared/', content)
        content = re.sub(r'href="/AlgorithmEcosystem/shared/', 'href="shared/', content)
        content = re.sub(r'href="shared/', 'href="shared/', content)
        
        # Fix JS paths
        content = re.sub(r'src="\.\./shared/', 'src="shared/', content)
        content = re.sub(r'src="/AlgorithmEcosystem/shared/', 'src="shared/', content)
        content = re.sub(r'src="shared/', 'src="shared/', content)
        
        # Add missing meta tags if not present
        if '<meta charset="UTF-8">' not in content:
            content = content.replace('<head>', '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Algorithm Ecosystem - Học thuật toán trực tuyến">
    <meta name="keywords" content="algorithms, programming, learning, coding">
    <meta name="author" content="Algorithm Ecosystem">
    <meta name="theme-color" content="#667eea">''')
        
        # Add service worker registration if not present
        if 'service-worker.js' not in content and '</body>' in content:
            service_worker_script = '''
    <script>
        // Register service worker for PWA
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('shared/service-worker.js')
                    .then(function(registration) {
                        console.log('ServiceWorker registration successful');
                    })
                    .catch(function(err) {
                        console.log('ServiceWorker registration failed');
                    });
            });
        }
    </script>'''
            content = content.replace('</body>', f'{service_worker_script}\n</body>')
        
        # Add back button if not present
        if 'Quay lại' not in content and 'Back' not in content:
            # Find a good place to add back button (usually after header)
            if '<header>' in content and '</header>' in content:
                back_button = '''
        <div style="margin: 20px 0;">
            <a href="index.html" class="btn btn-secondary" style="text-decoration: none; padding: 10px 20px; background: #6c757d; color: white; border-radius: 5px;">
                ← Quay lại trang chủ
            </a>
        </div>'''
                header_end = content.find('</header>') + len('</header>')
                content = content[:header_end] + back_button + content[header_end:]
        
        # Write back if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {file_path}")
        else:
            print(f"✅ No changes needed: {file_path}")
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """Main function to process all HTML files"""
    print("🚀 Starting HTML optimization...")
    
    # Get the current directory
    current_dir = Path.cwd()
    ui_dir = current_dir / "AlgorithmEcosystem" / "ui"
    
    if not ui_dir.exists():
        print(f"❌ UI directory not found: {ui_dir}")
        return
    
    # Find all HTML files
    html_files = list(ui_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ No HTML files found")
        return
    
    print(f"📁 Found {len(html_files)} HTML files")
    
    # Process each HTML file
    for html_file in html_files:
        fix_html_file(html_file)
    
    print("\n🎉 HTML optimization completed!")
    print(f"📊 Processed {len(html_files)} files")
    
    # Create a summary report
    print("\n📋 Summary of available pages:")
    for html_file in sorted(html_files):
        relative_path = html_file.relative_to(ui_dir)
        print(f"  - {relative_path}")

if __name__ == "__main__":
    main() 