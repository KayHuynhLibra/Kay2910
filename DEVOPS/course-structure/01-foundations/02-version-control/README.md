# Version Control

## Tổng quan
Module này cung cấp kiến thức về quản lý phiên bản với Git, từ cơ bản đến nâng cao, và áp dụng trong môi trường DevOps.

## Nội dung

### Tuần 1: Git Fundamentals
- Basic commands
  - init, clone, add, commit
  - push, pull, fetch
  - branch, checkout, merge
- Branching strategies
  - Git Flow
  - GitHub Flow
  - Trunk Based Development
- Merging và conflict resolution
  - Merge strategies
  - Resolving conflicts
  - Best practices
- Git workflows
  - Feature branches
  - Release branches
  - Hotfix branches

### Tuần 2: Advanced Git
- Git hooks
  - pre-commit
  - post-commit
  - pre-push
- Git submodules
  - Adding submodules
  - Updating submodules
  - Managing dependencies
- Git LFS
  - Large file handling
  - Configuration
  - Best practices
- Git internals
  - Objects
  - References
  - Index
  - Working directory

### Tuần 3: GitOps
- Infrastructure as Code
  - Version control for infrastructure
  - Configuration management
  - State management
- GitOps principles
  - Declarative configuration
  - Version controlled
  - Automated synchronization
  - Self-healing
- ArgoCD/Flux
  - Installation
  - Configuration
  - Application deployment
  - Sync policies
- Best practices
  - Security
  - Access control
  - Audit trails
  - Compliance

## Cấu trúc thư mục
```
02-version-control/
├── theory/
│   ├── 01-git-basics.md
│   ├── 02-git-advanced.md
│   └── 03-gitops.md
├── practice/
│   ├── exercises/
│   └── solutions/
├── labs/
│   ├── 01-git-workflow/
│   └── 02-gitops-setup/
└── projects/
    ├── 01-infrastructure-versioning/
    └── 02-gitops-implementation/
```

## Dự án
1. Infrastructure Versioning Project
   - Mục tiêu: Quản lý cấu hình infrastructure với Git
   - Kỹ năng: Git, Infrastructure as Code
   - Thời gian: 1 tuần

2. GitOps Implementation
   - Mục tiêu: Triển khai GitOps workflow
   - Kỹ năng: GitOps, ArgoCD/Flux
   - Thời gian: 1 tuần

## Tài liệu tham khảo
- Pro Git Book
- Git Documentation
- GitOps Principles
- ArgoCD Documentation 