# Version Control - Phần 2: Advanced Git

## 1. Git Internals
- Objects (blobs, trees, commits)
- References (heads, tags)
- Index (staging area)
- Working directory

## 2. Advanced Branching
```bash
# Rebase
git checkout feature
git rebase main
git rebase -i HEAD~3

# Cherry-pick
git cherry-pick commit_hash
git cherry-pick -x commit_hash

# Merge strategies
git merge -s recursive branch
git merge -s octopus branch1 branch2
git merge -s ours branch
```

## 3. Advanced Merging
```bash
# Resolve conflicts
git status
git diff
git add resolved_file
git commit

# Merge tools
git mergetool
git config --global merge.tool vimdiff

# Abort merge
git merge --abort
```

## 4. Git Hooks
```bash
# Pre-commit hook
#!/bin/sh
# Check code style
npm run lint

# Pre-push hook
#!/bin/sh
# Run tests
npm test

# Post-commit hook
#!/bin/sh
# Notify team
curl -X POST -H "Content-Type: application/json" \
     -d '{"message":"New commit"}' \
     http://notification-service
```

## 5. Git Submodules
```bash
# Add submodule
git submodule add https://github.com/username/repo.git

# Initialize submodules
git submodule init
git submodule update

# Update submodules
git submodule update --remote
```

## 6. Git Worktree
```bash
# Create worktree
git worktree add ../hotfix-branch hotfix

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../hotfix-branch
```

## 7. Git Bisect
```bash
# Start bisect
git bisect start
git bisect bad
git bisect good v1.0.0

# Run bisect
git bisect run npm test

# End bisect
git bisect reset
```

## 8. Git Blame và Log
```bash
# Blame
git blame file.txt
git blame -L 10,20 file.txt

# Log với filter
git log --author="John"
git log --since="2 weeks ago"
git log --grep="bug"
git log -S "function_name"
```

## 9. Git Reflog
```bash
# View reflog
git reflog
git reflog show HEAD

# Recover from reflog
git reset --hard HEAD@{1}
```

## 10. Git Clean và Maintenance
```bash
# Clean untracked files
git clean -n
git clean -f
git clean -fd

# Maintenance
git gc
git prune
git fsck
```

## 11. Git Config Advanced
```bash
# Aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch

# Credentials
git config --global credential.helper cache
git config --global credential.helper store

# Core settings
git config --global core.autocrlf input
git config --global core.ignorecase false
```

## 12. Git Workflows
### Gitflow
```bash
# Initialize gitflow
git flow init

# Feature
git flow feature start new-feature
git flow feature finish new-feature

# Release
git flow release start 1.0.0
git flow release finish 1.0.0

# Hotfix
git flow hotfix start bug-fix
git flow hotfix finish bug-fix
```

### Trunk Based Development
- Main branch always deployable
- Short-lived feature branches
- Continuous integration
- Automated testing

## 13. Git Security
- GPG signing
- Access control
- Audit logging
- Security scanning

## 14. Git Performance
- Shallow clones
- Partial clones
- Sparse checkouts
- Git LFS

## Bài tập thực hành
1. Sử dụng Git hooks
2. Quản lý submodules
3. Debug với Git bisect
4. Tối ưu hóa repository

## Tài liệu tham khảo
- Pro Git Book
- Git Documentation
- GitHub Guides
- Git Workflows 