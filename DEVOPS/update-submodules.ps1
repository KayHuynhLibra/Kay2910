# Update submodules script
# Script cập nhật submodule

$modules = @{
    "01-foundations" = @{
        "01-linux-fundamentals" = @("01-basic-commands", "02-file-system", "03-processes", "04-users-groups")
        "02-networking" = @("01-network-basics", "02-tcp-ip", "03-dns", "04-firewall")
        "03-system-admin" = @("01-system-monitoring", "02-backup-restore", "03-security", "04-automation")
        "04-scripting" = @("01-bash-scripting", "02-python-basics", "03-automation", "04-troubleshooting")
    }
    "02-version-control" = @{
        "01-git" = @("01-basic-commands", "02-branching", "03-merging", "04-advanced-features")
        "02-github" = @("01-repository-management", "02-collaboration", "03-actions", "04-security")
        "03-branching" = @("01-branch-strategies", "02-merge-strategies", "03-conflict-resolution", "04-best-practices")
    }
    "03-cicd" = @{
        "01-jenkins" = @("01-installation", "02-pipelines", "03-plugins", "04-integration")
        "02-github-actions" = @("01-workflows", "02-actions", "03-secrets", "04-self-hosted")
        "03-pipelines" = @("01-pipeline-design", "02-testing", "03-deployment", "04-monitoring")
    }
    "04-containerization" = @{
        "01-docker" = @("01-containers", "02-images", "03-networking", "04-volumes")
        "02-kubernetes" = @("01-cluster-setup", "02-pods-services", "03-deployments", "04-storage")
        "03-orchestration" = @("01-service-mesh", "02-monitoring", "03-security", "04-scaling")
    }
    "05-iac" = @{
        "01-terraform" = @("01-basics", "02-modules", "03-state", "04-best-practices")
        "02-ansible" = @("01-playbooks", "02-roles", "03-inventory", "04-templates")
        "03-cloudformation" = @("01-templates", "02-stacks", "03-parameters", "04-resources")
    }
    "06-monitoring" = @{
        "01-prometheus" = @("01-setup", "02-metrics", "03-alerting", "04-integration")
        "02-grafana" = @("01-dashboards", "02-visualization", "03-alerts", "04-plugins")
        "03-elk" = @("01-elasticsearch", "02-logstash", "03-kibana", "04-beats")
    }
    "07-security" = @{
        "01-fundamentals" = @("01-security-basics", "02-threat-modeling", "03-vulnerability", "04-compliance")
        "02-compliance" = @("01-standards", "02-auditing", "03-reporting", "04-remediation")
        "03-tools" = @("01-scanning", "02-monitoring", "03-automation", "04-incident-response")
    }
    "08-enterprise" = @{
        "01-architecture" = @("01-design", "02-scalability", "03-reliability", "04-cost-optimization")
        "02-deployment" = @("01-strategies", "02-automation", "03-monitoring", "04-disaster-recovery")
        "03-tools" = @("01-selection", "02-integration", "03-management", "04-maintenance")
    }
    "certifications" = @{
        "paths" = @("01-foundation", "02-intermediate", "03-advanced", "04-specialist")
        "resources" = @("01-study-materials", "02-practice-tests", "03-labs", "04-communities")
        "guides" = @("01-preparation", "02-exam-tips", "03-renewal", "04-career-path")
    }
}

foreach ($module in $modules.Keys) {
    foreach ($submodule in $modules[$module].Keys) {
        $basePath = "course-structure/$module/$submodule"
        
        # Create submodule directories
        foreach ($topic in $modules[$module][$submodule]) {
            $topicPath = "$basePath/$topic"
            New-Item -Path $topicPath -ItemType Directory -Force | Out-Null
            
            # Create standard subdirectories for each topic
            New-Item -Path "$topicPath/labs" -ItemType Directory -Force | Out-Null
            New-Item -Path "$topicPath/projects" -ItemType Directory -Force | Out-Null
            New-Item -Path "$topicPath/resources" -ItemType Directory -Force | Out-Null
            New-Item -Path "$topicPath/docs" -ItemType Directory -Force | Out-Null
        }
        
        # Create README.md for submodule
        $readmeContent = @"
# $submodule

## Overview
This submodule covers essential concepts and practices for $submodule.

## Topics
$($modules[$module][$submodule] -join "`n")

## Learning Objectives
- Understand core concepts
- Master practical skills
- Apply best practices
- Implement solutions

## Resources
- Documentation
- Tutorials
- Best Practices
- Tools

## Labs
- Hands-on exercises
- Real-world scenarios
- Troubleshooting
- Optimization

## Projects
- Implementation
- Integration
- Automation
- Monitoring

## Assessment
- Knowledge checks
- Practical exercises
- Project evaluation
- Certification preparation
"@
        
        Set-Content -Path "$basePath/README.md" -Value $readmeContent
    }
}

Write-Host "Submodule structure has been updated successfully."
Write-Host "Cấu trúc submodule đã được cập nhật thành công." 