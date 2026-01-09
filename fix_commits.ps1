# Script to fix commit messages using git filter-branch
$gitPath = "C:\Program Files\Microsoft SQL Server Management Studio 21\Release\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

# Change to project directory
Set-Location "C:\Users\abhis\OneDrive\Desktop\Fynd assignment"

# Use git filter-branch to rewrite commit messages
# This will rewrite history, so we'll need to force push after

Write-Host "Fixing commit messages..."
Write-Host "This will rewrite git history. Make sure you want to do this!"
Write-Host ""

# Map commit hashes to new messages
$commitMessages = @{
    "c751314" = "Rewrite docs to sound more natural"
    "923a188" = "Add all remaining project files"
    "5d4c61c" = "Update README status"
    "6e869b9" = "Add notebook and report"
    "8148e11" = "Improve user dashboard UI"
    "7f73e61" = "Redesign admin dashboard"
    "50acc39" = "Fix stats display and timezone"
    "25adeba" = "Update stats design"
    "0b62c83" = "Add Render deployment config"
}

# Use git rebase with a script that modifies messages
$rebaseScript = @"
`$content = Get-Content `$args[0]
foreach (`$line in `$content) {
    if (`$line -match '^pick (c751314|923a188|5d4c61c|6e869b9|8148e11|7f73e61|50acc39|25adeba|0b62c83)') {
        `$hash = `$matches[1]
        if (`$commitMessages.ContainsKey(`$hash)) {
            Write-Output "reword `$hash `$(`$commitMessages[`$hash])"
        } else {
            Write-Output `$line
        }
    } else {
        Write-Output `$line
    }
}
"@

Write-Host "Run this manually:"
Write-Host "git rebase -i HEAD~10"
Write-Host ""
Write-Host "Then change these commits from 'pick' to 'reword' and use these messages:"
foreach ($hash in $commitMessages.Keys) {
    Write-Host "$hash -> $($commitMessages[$hash])"
}
