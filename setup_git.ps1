# Git Setup Script
# Run this script after Git is installed

Write-Host "Initializing Git repository..." -ForegroundColor Green

# Initialize git repository
git init

# Add remote repository
git remote add origin https://github.com/abhi8927/Rating-Prediction-via-Prompting-Fynd.git

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Add README and .gitignore"

# Set main branch
git branch -M main

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor Green
git push -u origin main

Write-Host "Done! Repository is now connected to GitHub." -ForegroundColor Green
