# Script to fix commit messages to sound more human
# This will require force push after: git push --force origin main

$gitPath = "C:\Program Files\Microsoft SQL Server Management Studio 21\Release\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

# Map of old commit messages to new ones (more casual)
$messageMap = @{
    "Rewrite all documentation in natural human language" = "Rewrite docs to sound less AI-generated"
    "Final commit: All project files, improvements, and documentation" = "Add all remaining project files"
    "Update README with completed deliverables and current status" = "Update README with what's done"
    "Add Task 1 Jupyter notebook and project report" = "Add notebook and report"
    "Enhance User Dashboard with rating labels, better success state, and improved UI elements" = "Improve user dashboard UI"
    "Redesign admin dashboard with bar chart stats, star icons, and improved layout" = "Redesign admin dashboard layout"
    "Redesign stats with professional clean design, remove emojis, fix Indian timezone formatting" = "Fix stats display and timezone"
    "Enhance stats display with modern professional design including percentages and visual indicators" = "Update stats display design"
    "Add Render deployment configuration files" = "Add files for Render deployment"
}

Write-Host "To fix commit messages, use interactive rebase:"
Write-Host "git rebase -i HEAD~10"
Write-Host ""
Write-Host "Then change 'pick' to 'reword' for commits you want to edit, and change messages to:"
Write-Host ""
foreach ($old in $messageMap.Keys) {
    Write-Host "Old: $old"
    Write-Host "New: $($messageMap[$old])"
    Write-Host ""
}
