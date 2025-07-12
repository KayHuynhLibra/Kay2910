# Cleanup script for course structure
# Script dọn dẹp cấu trúc khóa học

# Remove duplicate directories
# Xóa các thư mục trùng lặp
Remove-Item -Path "course-structure/07-enterprise" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/06-security" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/08-security" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/03-cloud" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/07-cloud" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/05-monitoring" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/04-iac" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/04-cicd" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/03-container" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/09-enterprise-deployment" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/04-advanced-topics" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/03-cicd-automation" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "course-structure/02-cloud-infrastructure" -Recurse -Force -ErrorAction SilentlyContinue

# Create standard directory structure
# Tạo cấu trúc thư mục chuẩn
$modules = @(
    "01-foundations",
    "02-version-control",
    "03-cicd",
    "04-containerization",
    "05-iac",
    "06-monitoring",
    "07-security",
    "08-enterprise",
    "certifications"
)

$submodules = @{
    "01-foundations" = @("01-linux-fundamentals", "02-networking", "03-system-admin", "04-scripting")
    "02-version-control" = @("01-git", "02-github", "03-branching")
    "03-cicd" = @("01-jenkins", "02-github-actions", "03-pipelines")
    "04-containerization" = @("01-docker", "02-kubernetes", "03-orchestration")
    "05-iac" = @("01-terraform", "02-ansible", "03-cloudformation")
    "06-monitoring" = @("01-prometheus", "02-grafana", "03-elk")
    "07-security" = @("01-fundamentals", "02-compliance", "03-tools")
    "08-enterprise" = @("01-architecture", "02-deployment", "03-tools")
    "certifications" = @("paths", "resources", "guides")
}

foreach ($module in $modules) {
    # Create module directory
    # Tạo thư mục module
    New-Item -Path "course-structure/$module" -ItemType Directory -Force | Out-Null

    # Create submodule directories
    # Tạo thư mục submodule
    foreach ($submodule in $submodules[$module]) {
        $path = "course-structure/$module/$submodule"
        New-Item -Path $path -ItemType Directory -Force | Out-Null
        
        # Create standard subdirectories
        # Tạo các thư mục con chuẩn
        New-Item -Path "$path/labs" -ItemType Directory -Force | Out-Null
        New-Item -Path "$path/projects" -ItemType Directory -Force | Out-Null
        New-Item -Path "$path/resources" -ItemType Directory -Force | Out-Null
    }
}

Write-Host "Directory structure has been cleaned up and reorganized."
Write-Host "Cấu trúc thư mục đã được dọn dẹp và tổ chức lại." 